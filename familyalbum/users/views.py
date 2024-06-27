from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView, PasswordResetView, PasswordResetConfirmView
from django.views.generic.edit import FormView
from .forms import RegisterForm, MyLoginForm, MyPasswordResetForm, MyPasswordResetConfirmForm, UserUpdateForm, ProfileUpdateForm
from django.contrib.auth import login
from django.urls import reverse_lazy
from django.contrib import messages
from django.views import View


# Create your views here.

class MyLoginView(LoginView):
    redirect_authenticated_user = True
    template_name = "users/login.html"
    form_class = MyLoginForm

    def form_invalid(self, form):
        messages.error(self.request, 'invalid username or password')
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


class MyProfile(View):
    def get(self, request):
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user.profile)
        context = {
            'user_form':user_form,
            'profile_form':profile_form
        }

        return render(request, 'users/profile.html', context)

    def post(self, request):
        user_form = UserUpdateForm(
            request.POST,
            instance=request.user
        )

        profile_form = ProfileUpdateForm(
            request.POST,
            request.FILES,
            instance=request.user.profile
        )

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Your profile has been updated successfully')
            return redirect('profile')
        else:
            messages.error(request, "Error updating your profile")
            context = {
            'user-form':user_form,
            'profile_form':profile_form
            }
        return render(request, 'users/profile.html', context)