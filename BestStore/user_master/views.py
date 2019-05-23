import json
from django.http import Http404
from django.shortcuts import render
from django.http import JsonResponse
from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.contrib.auth import login
from django.contrib.auth import logout
from django.core.mail import send_mail
from django.utils.html import strip_tags
from django.views.generic import UpdateView
from django.views.generic import DeleteView
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.template.loader import render_to_string
from django.contrib.auth.hashers import make_password
from django.contrib.auth.mixins import LoginRequiredMixin


def register_user(request):
    """This function will register a user"""
    if request.method == 'POST':
        body = json.loads(request.body)
        user_dict = {key: body[key] for key in ('username', 'first_name', 'last_name')}
        user_dict.update({
            'password': make_password(body['password']), 
            'email': user_dict['username'],
            'is_active': False
        })
        try:
            new_user = User(**user_dict)
            new_user.save()
            url = f"http://127.0.0.1:8000/api/user/verify/{new_user.password.replace('/','*')}"
            full_name = f'{new_user.first_name} {new_user.last_name}'
            context = {'action': 'Confirm Email', 'url': url, 'full_name': full_name}
            html_message = render_to_string('master/email.html', context)
            plain_message = strip_tags(html_message)
            send_mail('Best Store Account Confirmation',
                      plain_message,
                      'admin@thebeststore.com',
                      [new_user.email],
                      html_message=html_message,
                      fail_silently=False)
            json_res = {'success': True}
            return JsonResponse(json_res)
        except Exception:
            json_res = {'success': False, 'error': 'Email already in use.'}
            return JsonResponse(json_res)


def user_login(request):
    """This is a login function using Django's inbuilt login functionality"""
    body = json.loads(request.body)
    username, password = body['email'], body['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        name = user.first_name
        request.session['username'] = name
        login(request, user)
        json_res = {'success': True}
        return JsonResponse(json_res)
    else:
        json_res = {'success': False}
        return JsonResponse(json_res)


def verify_user_email(request, token):
    """Confirming the user email"""
    user = User.objects.get(password=token.replace("*", "/"))
    if user is not None:
        user.is_active = True
        user.save()
        return redirect('/')
    else:
        raise Http404

        
def logout_view(request):
    """Logging off the user"""
    logout(request)
    return redirect("homepage")


def user_dashboard(request):
    """This will show the user dashboard."""
    return render(request, "user_master/dashboard.html")


class UpdateUserProfile(LoginRequiredMixin, UpdateView):
    """Update the user's first name, last name and Email"""
    model = User
    fields = ['first_name', 'last_name', 'email']
    template_name = 'user_master/user_update_form.html'

    def get_object(self, queryset=None):
        """This will verify if the current user is updating his profile or not"""
        current_user = super(UpdateUserProfile, self).get_object(queryset)
        if current_user.username != self.request.user.username:
            raise Http404("Company does not exist")
        return current_user


class DeleteUserProfile(LoginRequiredMixin, DeleteView):
    """Deletes the user profile """
    model = User
    success_url = reverse_lazy('login')
    template_name = 'user_master/user_confirm_delete.html'
