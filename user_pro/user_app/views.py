from django.shortcuts import render, redirect
from .forms import (User, UserForm, UserUpdateForm, PasswordChangeForm, UserPasswordOtpForm,
                    UserPasswordResetForm)
from django.contrib.auth.decorators import login_required
from django.contrib import messages
# Create your views here.


def create_user_view(request):
    form = UserForm()
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('users')
    context = {"form":form}
    template_name = 'user_app/user_form.html'
    return render(request, template_name, context)

@login_required(login_url='/login/')
def show_user_view(request):
    data = User.objects.all()
    context = {"data":data}
    template_name = 'user_app/show_user.html'
    return render(request, template_name, context)

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
        return redirect('users')
    template_name = 'user_app/delete_confirm_form.html'
    return render(request, template_name)

def password_change_view(request):
    form = PasswordChangeForm(request.user)
    if request.method == "POST":
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            form.save()
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
