from django.shortcuts import render
from django.template import Template
from .models import Customer,Menu,Address, Cart, Orders
from django.contrib.auth.hashers import make_password
from django.http import JsonResponse
import json
import jwt
import uuid

# Create your views here.
def home(request):
    return render(request,'home.html')

def login(request):
    
    if request.method == 'POST':

        try :
            data = json.loads(str(request.body, encoding='utf-8'))
            email = data['email']
            password = data['password']
            # check if customer exists
            try:
                customer = Customer.objects.get(email=email)
            except:
                return JsonResponse({'success': False,'error':'Customer does not exist'})
            is_email = Customer.objects.filter(email=email).exists()
            password_database = Customer.objects.filter(email=email).values('password')
            is_password = customer.check_password(password)
            # if password is incorrect
            if not is_password:
                return JsonResponse({'success': False,'error':'Password/Email is incorrect'})
            
            customer_login = Customer.objects.get(email=email)
            token = jwt_token_handler(customer_login)
            return JsonResponse({'success': True,'error': 'null','token':token})
        except Exception as e:
            print(e)
            return JsonResponse({'success': False,'error':'Something went wrong / Invalid data'})  
    
    return render(request,'login.html')

def register(request):

    if request.method == 'POST':
        try:
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
        
        except Exception as e:
            print(e)
            return JsonResponse({'success': False,'error':'Something went wrong / Invalid data'})
    return render(request,'signup.html')

def menu(request):
    menu_items = Menu.objects.all()
    items = {'menu_items':menu_items}
    return render(request,'menu.html',items)

def add_to_cart(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        item_id = data['item_id']
        auth_token = request.headers['Authorization']
        token = auth_token.split(' ')[1]
        token_payload = jwt.decode(token,'secret',algorithms=['HS256'])
        user_uuid = token_payload['uuid']
        user_email = token_payload['email']
        
        customer = Customer.objects.get(email=user_email, uuid=user_uuid)
        item = Menu.objects.get(id=item_id)
        cart = Cart.objects.create(customer=customer,item=item)
        cart.save()
        
        print(token_payload)
        print(item_id)
        
    return JsonResponse({'success': True,'error': 'null'})

def remove_from_cart(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        item_id = data['item_id']
        auth_token = request.headers['Authorization']
        token = auth_token.split(' ')[1]
        token_payload = jwt.decode(token,'secret',algorithms=['HS256'])
        user_uuid = token_payload['uuid']
        user_email = token_payload['email']
        
        customer = Customer.objects.get(email=user_email, uuid=user_uuid)
        item = Menu.objects.get(id=item_id)
        cart = Cart.objects.get(customer=customer,item=item)
        cart.delete()
        print(token_payload)
        print(item_id)
    return JsonResponse({'success': True,'error': 'null'})



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

