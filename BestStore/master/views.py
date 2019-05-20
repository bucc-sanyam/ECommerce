from django.shortcuts import render
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags

html_message = render_to_string('master/email.html', {'context': 'values'})
plain_message = strip_tags(html_message)


def home(request):
    send_mail('Best Store Account Confirmation', plain_message, 'yamalik42@gmail.com', ['yash.malik@tothenew.com'], html_message=html_message, fail_silently=False,)
    return render(request, "master/homepage.html")


def register(request):
    return render(request, "master/register.html")


def render_login_form(request):
    return render(request, 'master/login.html')