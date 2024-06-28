from django.urls import path
from .views import MyLoginView, RegisterView, MyPasswordResetView, MySetPasswordResetView
from django.contrib.auth.views import LogoutView, PasswordResetDoneView, PasswordResetCompleteView

urlpatterns = [
    path('login/', MyLoginView.as_view(), name='login'),
    path('register/', RegisterView.as_view(), name='register'),
    path('logout/', LogoutView.as_view(next_page="home"), name='logout'),
    path('password-reset/', MyPasswordResetView.as_view(template_name='users/password_reset.html', from_email = 'artem.lipatov.91@mail.ru'), name='password_reset'),
    path('password-reset/done/', PasswordResetDoneView.as_view(template_name='users/password_reset_done.html'), name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/', MySetPasswordResetView.as_view(template_name='users/password_reset_confirm.html'), name='password_reset_confirm'),
    path('password-reset/complete/', PasswordResetCompleteView.as_view(template_name='users/password_reset_complete.html'), name='password_reset_complete'),
]