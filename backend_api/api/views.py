from django.shortcuts import render  
from .models import User
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['POST'])
def register(request):
    username = request.data.get('username')
    email = request.data.get('email')
    password = request.data.get('password')
def login(request):
    return Response({"message": "تم إنشاء مسار الـ Login بنجاح!"})    
    
    first_name = request.data.get('first_name')
    last_name = request.data.get('last_name')
    phone = request.data.get('phone')
    age = request.data.get('age')
    address = request.data.get('address')

    
    if User.objects.filter(username=username).exists():
        return Response({"status": False, "message": "Username already exists"})
        
    if User.objects.filter(email=email).exists():
        return Response({"status": False, "message": "Email already exists"})


    User.objects.create(
        username=username,
        email=email,
        password=password,
        first_name=first_name,
        last_name=last_name,
        phone=phone,
        age=age,
        address=address
    )

    return Response({"status": True, "message": "User registered successfully"})