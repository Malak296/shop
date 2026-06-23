from django.contrib.auth.models import User
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth import authenticate

@api_view(['POST'])
def register(request):
    username = request.data.get('username')
    email = request.data.get('email')
    password = request.data.get('password')

    if User.objects.filter(username=username).exists():
        return Response({
            "status": False,
            "message": "Username already exists"
        })

    User.objects.create_user(
        username=username,
        email=email,
        password=password
    )

    return Response({
        "status": True,
        "message": "User created successfully"
    })


@api_view(['POST'])
def login(request):
    username = request.data.get('username')
    password = request.data.get('password')

    user = authenticate(
        username=username,
        password=password
    )

    if user is not None:
        return Response({
            "status": True,
            "message": "Login successful"
        })

    return Response({
        "status": False,
        "message": "Invalid username or password"
    })