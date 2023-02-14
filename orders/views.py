from django.shortcuts import render
from django.template import Template
from .models import Customer,Burger,Address
from django.contrib.auth.hashers import make_password
from django.shortcuts import redirect
import datetime
from django.conf import settings
from django.http import HttpResponse, JsonResponse
import json
import jwt
import uuid

# Create your views here.
def home(request):
    return render(request,'home.html')

def login(request):
    
    if request.method == 'POST':
        data = json.loads(request.body)
        email = data['email']
        password = data['password']
        # check if email exists
        is_email = Customer.objects.filter(email=email).exists()
        password_database = Customer.objects.filter(email=email).values('password')
        is_password = make_password(password) == password_database[0]['password']
        if not is_email:
            return JsonResponse({'success': False,'error':'Customer does not exists'})
        
        if not is_password:
            return JsonResponse({'success': False,'error':'Password incorrect'})
    
    return render(request,'login.html')

def register(request):

    if request.method == 'POST':
        data = json.loads(request.body)
        first_name = data['first_name']
        last_name = data['last_name']
        email = data['email']
        password = data['password']
        password1 = data['confirm_password']
        phone = data['phone']
        address = data['address']
        city = data['city']
        state = data['state']
        pin = data['pin']
        user_uuid = uuid.uuid4()
        user = {'first name':first_name,'last_name':last_name,'email':email,'phone':phone,'address':address,'city':city,'state':state,'pin':pin}

        
        # if email already exists
        is_email = Customer.objects.filter(email=email).exists()
        if is_email:
            return JsonResponse({'success': False,'error':'Email already exists','user':user})

        # if password does not match
        if password != password1:
            return JsonResponse({'success': False,'error':'Password does not match','user':user})

        encrypted_password = make_password(password)
        customer = Customer.objects.create(first_name=first_name,last_name=last_name,email=email,password=encrypted_password,phone=phone,uuid=user_uuid)
        customer.save()
        customer_address = Address.objects.create(customer=customer,address=address,city=city,state=state,pin=pin)
        customer_address.save()
        
        
        # refresh token for user

        token_payload = {
            'first name':first_name,
            'last_name':last_name,
            'email':email,
            'uuid': str(user_uuid),
        }
        token = jwt.encode(token_payload,'secret',algorithm='HS256')
        print(token)
        return JsonResponse({'success': True,'error': 'null','token':token})
    return render(request,'signup.html')