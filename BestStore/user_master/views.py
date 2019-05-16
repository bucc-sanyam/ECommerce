from django.shortcuts import render
from django.http import JsonResponse
from .models import Merchant
from django.contrib.auth.models import User
import json
from django.core.mail import send_mail

# Create your views here.
def testpost(request):
    if request.method == 'POST':
        body = json.loads(request.body)
        user_keys = ('username', 'password', 'first_name', 'last_name')
        user_dict = { key: body[key] for key in user_keys }
        try:
            new_user = User(**user_dict)
            new_user.save()
            json_res = {'success': True}
            send_mail('Best Store Account Confirmation', 'Please click the following link to confirm your email and validate your account.', 'yamalik42@gmail.com', ['yash.malik@tothenew.com'], fail_silently=False,)
            return JsonResponse(json_res)
        except Exception:
            json_res = {'success': False, 'error': 'Email already in use.'}
            return JsonResponse(json_res)

