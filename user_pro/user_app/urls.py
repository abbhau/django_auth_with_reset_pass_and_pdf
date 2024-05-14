from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import (create_user_view, show_user_view, update_user_view, delete_user_view, 
                    password_change_view , password_reset_email_send_view, password_reset_view)
urlpatterns = [
    path('users/', show_user_view, name='users'),
    path('user/create/', create_user_view, name='user-create'),
    path('user/update/<int:pk>/', update_user_view, name='user-update'),
    path('user/delete/<int:pk>/', delete_user_view, name='user-delete'),
    path('login/' , LoginView.as_view(template_name='user_app/user_form.html', next_page='users'), name="login"),
    path('logout/' , LogoutView.as_view(next_page='/login/'), name='logout'),
    path('users/password/change/', password_change_view , name='user-password-change'),
    path('users/password/reset/link/', password_reset_email_send_view, name='user-password-reset-link'),
    path('users/password/reset/set/', password_reset_view, name='user-password-_set_reset'),
]