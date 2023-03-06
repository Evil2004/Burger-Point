from django.shortcuts import render
from django.template import Template
from .models import Customer,Menu,Address, Cart, Orders
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
        print(request.body)
        data = json.loads(str(request.body, encoding='utf-8'))
        
        email = data['email']
        password = data['password']
        # check if email exists
        is_email = Customer.objects.filter(email=email).exists()
        password_database = Customer.objects.filter(email=email).values('password')
        is_password = make_password(password) == password_database[0]['password']
        
        if not is_email:
            return JsonResponse({'success': False,'error':'Customer does not exists'})
        # if password is incorrect
        if not is_password:
            return JsonResponse({'success': False,'error':'Password/Email is incorrect'})
        
        customer_login = Customer.objects.get(email=email)
        token = jwt_token_handler(customer_login)
        return JsonResponse({'success': True,'error': 'null','token':token})
    
    return render(request,'login.html')

def register(request):

    if request.method == 'POST':
        print(request.body)
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
            return JsonResponse({'success': False,'error':'Email already exists',})
        
        is_phone = Customer.objects.filter(phone=phone).exists()
        if is_phone:
            return JsonResponse({'success': False,'error':'Phone number already exists',})

        # if password does not match
        if password != password1:
            return JsonResponse({'success': False,'error':'Password does not match',})

        encrypted_password = make_password(password)
        customer = Customer.objects.create(first_name=first_name,last_name=last_name,email=email,password=encrypted_password,phone=phone,uuid=user_uuid)
        customer.save()
        customer_address = Address.objects.create(customer=customer,address=address,city=city,state=state,pin=pin)
        customer_address.save()
        
        
        # refresh token for user

        token = jwt_token_handler(customer)
        print(type(token))
        return JsonResponse({'success': True,'error': 'null','token':str(token)})
    return render(request,'signup.html')

def menu(request):
    
    menu_items = Menu.objects.all()
    print(menu_items)
    items = {'menu_items':menu_items}
    return render(request,'menu.html',items)



# to generate token for customer utility function
def jwt_token_handler (customer):
    token_payload = {
        'first_name':customer.first_name,
        'last_name':customer.last_name,
        'email':customer.email,
        'uuid': str(customer.uuid),
    }
    token = jwt.encode(token_payload,'secret',algorithm='HS256')
    return token

