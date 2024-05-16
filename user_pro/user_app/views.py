from django.shortcuts import render, redirect
from django.http.response import HttpResponse, JsonResponse
from .forms import (User, UserForm, UserUpdateForm, PasswordChangeForm, UserPasswordOtpForm,
                    UserPasswordResetForm, TotalPrize)
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
import pdfkit
from django.template import loader
# Create your views here.



def create_user_view(request):
    form = UserForm()
    print(form)
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('users')
    context = {"form":form}
    template_name = 'user_app/user_form.html'
    return render(request, template_name, context)


class show_user_view(LoginRequiredMixin, View):
    login_url = '/login/'
    def get(self, request):
        data = User.objects.all()
        context = {"data":data}
        template_name = 'user_app/show_user.html'

        template = loader.get_template(template_name)
        page = template.render(context, request)
        pdfkit.from_string(page, 'media/pdf/users_list.pdf')
        return HttpResponse(page)


def download_pdf(request):
    users = User.objects.all()
    template = loader.get_template('user_app/show_user copy.html')
    page = template.render({'data': users}, request)
    options = {
        'page-size': 'A4',
        'encoding': "UTF-8",
    }
    pdf = pdfkit.from_string(page, False, options)
    response = HttpResponse(pdf, content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="user_list.pdf" '
    return response    

@login_required(login_url='/login/')
def update_user_view(request, pk=None):
    obj = User.objects.get(id=pk)
    form = UserUpdateForm(instance=obj)
    if request.method == "POST":
        form = UserUpdateForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return redirect('users')
    context = {"form":form}
    template_name = 'user_app/user_form.html'
    return render(request, template_name, context)

@login_required(login_url='/login/')
def delete_user_view(request, pk=None):
    obj = User.objects.get(id=pk)
    if request.method == "POST":
        obj.delete()
        messages.error(request, "Record deleted.")
        return redirect('users')
    template_name = 'user_app/delete_confirm_form.html'
    return render(request, template_name)

def password_change_view(request):
    form = PasswordChangeForm(request.user)
    if request.method == "POST":
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "password change successfully , plz login again ....")
            return redirect('login')
    context = {"form":form}
    template_name = 'user_app/user_form.html'
    return render(request, template_name, context)

def password_reset_email_send_view(request):
    form = UserPasswordOtpForm()
    if request.method == "POST":
        form = UserPasswordOtpForm(request.POST)
        if form.is_valid():
            return redirect('user-password-_set_reset')
    context = {"form":form}
    template_name = 'user_app/user_form.html'
    return render(request, template_name, context)

def password_reset_view(request):
    form = UserPasswordResetForm()
    if request.method == "POST":
        form = UserPasswordResetForm(request.POST)
        if form.is_valid():
            messages.success(request, "password reset successfully.")
            return redirect('login')
    context = {"form":form}
    template_name = 'user_app/user_form.html'
    return render(request, template_name, context)

class prize_view(View):
    def get(self, request):
        form = TotalPrize()
        context = {"form":form}
        template_name = 'user_app/javascript_form.html'
        template = loader.get_template(template_name)
        return HttpResponse(template.render(context, request))

class user_specific_view(View):
    def get(self, request, pk):
        obj = User.objects.filter(id=pk)
        context={"data":obj}
        template_name = 'user_app/show_user_detail.html'
        template = loader.get_template(template_name)
        return HttpResponse(template.render(context, request))

def download_pdf_single(request, pk=None):
    users = User.objects.filter(id=pk)
    template = loader.get_template('user_app/show_user_detail.html')
    page = template.render({'data': users}, request)
    options = {
        'page-size': 'A4',
        'encoding': "UTF-8",
    }
    pdf = pdfkit.from_string(page, False, options)
    response = HttpResponse(pdf, content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="user_detail.pdf" '
    return response    

