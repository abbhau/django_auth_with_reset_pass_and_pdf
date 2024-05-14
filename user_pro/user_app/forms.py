from django.contrib.auth.models import User
from django.contrib.auth.forms import (UserCreationForm, PasswordChangeForm, PasswordResetForm,
                                       SetPasswordForm)
from django import forms
from django.core.exceptions import ValidationError
from .models import UserOtp
import random
from django.conf import settings
from django.core.mail import send_mail
from django.core.exceptions import ValidationError
class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']


    def clean_email(self):
        email = self.cleaned_data['email']
        if not email.endswith("@gmail.com"):
             raise ValidationError("only @gmail.com domain allowed")
        return email

class UserUpdateForm(forms.ModelForm):
    #password = forms.CharField(disabled=True)
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']
    
    def clean_email(self):
        email = self.cleaned_data['email']
        if not email.endswith("@gmail.com"):
            raise ValidationError("only @gmail.com domain allowed")
        return email
    
    def save(self, commit=True):

        form = self
        print("form-----",form)

class UserPasswordOtpForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['email']

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            user = User.objects.get(email=email)
            otp = "".join([str(random.randint(1,9)) for _ in range(6)])
            ema = UserOtp.objects.filter(email=email)
            if ema:
                print(ema.delete())
                print(ema)
            obj, created= UserOtp.objects.get_or_create(email=email, otp=otp)
            print(obj.otp, created)
            subject = 'welcome to splendornet technologies'
            message = f'Hi {user.first_name , user.last_name} your password reset otp is : {obj.otp}'
            from_email = settings.EMAIL_HOST_USER
            recipient_list = [user.email, ]
            
            send_mail( subject, message,  from_email , recipient_list )
            return email
        else:
            raise ValidationError("email does not exist")
        
class UserPasswordResetForm(forms.ModelForm):
    otp = forms.CharField(max_length=6)
    password1 = forms.CharField(widget=forms.PasswordInput(), label='Password')
    password2 = forms.CharField(widget=forms.PasswordInput(), label='Confirm_Password')
    class Meta:
        model = User
        fields = ['email','otp', 'password1', 'password2']

    def clean(self):
        attr = super().clean()
        ps1 = attr.get('password1')
        ps2 = attr.get('password2')
        if ps1!=ps2:
            raise ValidationError("password and confirm password dosent match")
        return attr
    
    def clean(self):
        attr = super().clean()
        email = attr.get('email')
        otp = attr.get('otp')
        ps1 = attr.get('password1')
        obj1 = UserOtp.objects.filter(email=email).exists()
        if obj1:
            obj = UserOtp.objects.get(email=email)
            if obj.otp == otp:
                user = User.objects.get(email=email)
                user.set_password(ps1)
                user.save()
                obj.delete()
                return attr
            else:
                raise ValidationError("Invalid otp")
        else:
            raise ValidationError("email does not exist")

        
        
         
    



