from django.contrib.auth.views import LoginView, PasswordResetView, PasswordResetConfirmView
from django.views.generic.edit import FormView
from .forms import RegisterForm, MyLoginForm, MyPasswordResetForm, MyPasswordResetConfirmForm
from django.contrib.auth import login
from django.urls import reverse_lazy
from django.contrib import messages



# Create your views here.

class MyLoginView(LoginView):
    redirect_authenticated_user = True
    template_name = "users/login.html"
    form_class = MyLoginForm

    def form_invalid(self, form):
        messages.error(self.request, 'Неправильный логин или пароль')
        return self.render_to_response(self.get_context_data(form=form))
    
    def get_success_url(self):
        return reverse_lazy('home_user')

class RegisterView(FormView):
    template_name = 'users/register.html'
    form_class = RegisterForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('home_user')

    def form_valid(self, form):
        user = form.save()
        if user:
            login(self.request, user)
        return super(RegisterView, self).form_valid(form)
    
class MyPasswordResetView(PasswordResetView):
    form_class = MyPasswordResetForm

class MySetPasswordResetView(PasswordResetConfirmView):
    form_class = MyPasswordResetConfirmForm
