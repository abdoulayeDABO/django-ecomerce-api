from django.views.decorators.http import require_http_methods
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.core.mail import send_mail
import json
from django.http import HttpResponse
from django.core.exceptions import ValidationError
from ..decorators.auth import login_required
from ..serializer import UserSerializer
from ..models import Customer
from ..utils import generate_otp, send_email, HTTPResponse, is_otp_valid
from datetime import datetime, timedelta
from django.contrib.auth.hashers import make_password, check_password, is_password_usable
import jwt
from dotenv import dotenv_values
config = dotenv_values(".env")


@require_http_methods(["POST"])
@csrf_exempt
def login(request):
    response = {
        'status': 'error',
        'message': ''
    }
    try:
        data = json.loads(request.body)
        user = Customer.objects.filter(email=data['email']).first()
        if not user:
            response['message'] = 'User not found'
            return HTTPResponse(response, 400)
        if not user.is_confirmed:
            response['message'] = 'Account not activated'
            return HTTPResponse(response, 400)
        if not user.check_password(data['password']):
            response['message'] = 'Invalid password'
            return HTTPResponse(response, 400)
        secret_token = jwt.encode(
            {"token": user.id}, config['JWT_SECRET'], algorithm="HS256")
        return HTTPResponse({'status': 'success', 'message': 'Login successful', 'data': {"user": UserSerializer(user).data, "secret_token": secret_token}}, 200)

    except Exception as e:
        response['message'] = f"Error while logging in {str(e)}"
        return HTTPResponse(response, 500)


@require_http_methods(["POST"])
@csrf_exempt
def register(request):
    """ Register a new user """
    try:
        data = json.loads(request.body)
        # print(data)
        user = Customer.objects.filter(email=data['email']).first()
        if user:
            response = {
                'status': 'error',
                'message': 'User already exists'
            }
            return HTTPResponse(response, 409)

        hashed_password = make_password(data['password'])
        user = Customer.objects.create(
            email=data['email'],
            password=hashed_password,
            otp=generate_otp(),
            otp_expires_at=datetime.now() + timedelta(minutes=5),  # Expires in 5 minutes
        )

        send_email(
            "Activate your account",
            "This is your activation email. \n Otp is " + user.otp,
            "admin@example.com",
            user.email,
        )

        if user:
            userData = UserSerializer(user).data
            response = {
                'status': 'success',
                'message': 'User registered successfully',
                'data': userData
            }
        return HTTPResponse(response, 201)

    except Exception as e:
        response = {
            'status': 'error',
            'message': f"Error while registering user {str(e)} Try again later",
        }
        return HTTPResponse(response, 500)


@require_http_methods(["POST"])
@csrf_exempt
def activate_account(request):
    """ Activate an account """
    try:
        data = json.loads(request.body)
        user = Customer.objects.filter(email=data['email']).first()
        if not user:
            response = {
                'status': 'error',
                'message': 'User not found'
            }
            return HTTPResponse(response, 400)

        if not is_otp_valid(data['otp'], user.otp, user.otp_expires_at):
            response = {
                'status': 'error',
                'message': 'Otp is incorrect or expired'
            }
            return HTTPResponse(response, 400)
        user.is_confirmed = True
        user.otp = None
        user.otp_expires_at = None
        user.save()
        response = {
            'status': 'success',
            'message': 'Account activated successfully'
        }
        return HTTPResponse(response, 200)
    except Exception as e:
        response = {
            'status': 'error',
            'message': "Error while activating account" + str(e),
        }
        return HTTPResponse(response, 400)


@require_http_methods(["POST"])
@csrf_exempt
def resend_activation_email(request):
    if request.method == "POST":
        data = json.loads(request.body)
        user = Customer.objects.filter(email=data['email']).first()
        if not user:
            response = {
                'status': 'error',
                'message': 'User not found'
            }
            return HTTPResponse(response, 400)
        send_email(
            "Activate your account",
            "This is your activation email. \n Otp is " + user.otp,
            "admin@example.com",
            user.email,
        )
        response = {
            'status': 'success',
            'message': 'Email sent successfully'
        }
        return HTTPResponse(response, 200)


@require_http_methods(["POST"])
@csrf_exempt
@login_required
def logout(request):
    return HttpResponse("Logout successful")


@require_http_methods(["POST"])
@csrf_exempt
def forgot_password(request):
    return HttpResponse("Forgot password successful")


@require_http_methods(["POST"])
@csrf_exempt
def verify_email(request):
    return HttpResponse("Verify email successful")


@require_http_methods(["POST"])
@csrf_exempt
def confirm_reset_password(request):
    return HttpResponse("Confirm reset password successful")


@require_http_methods(["POST"])
@csrf_exempt
def reset_password(request):
    return HttpResponse("Reset password successful")


@require_http_methods(["POST"])
@csrf_exempt
@login_required
def change_password(request):
    try:
        data = json.loads(request.body)
        user = Customer.objects.filter(email=data['email']).first()
        if not user:
            response = {
                'status': 'error',
                'message': 'User not found'
            }
            return HTTPResponse(response, 400)
        if not user.check_password(data['password']):
            response = {
                'status': 'error',
                'message': 'Invalid password'
            }
            return HTTPResponse(response, 400)
        user.password = make_password(data['password'])
        user.save()
        response = {
            'status': 'success',
            'message': 'Password changed successfully'
        }
        return HTTPResponse(response, 200)
    except Exception as e:
        response = {
            'status': 'error',
            'message': "Error while changing password",
        }
        return HTTPResponse(response, 400)


@require_http_methods(["POST"])
@csrf_exempt
@login_required
def update_profile(request):
    try:
        data = json.loads(request.body)
        user = Customer.objects.filter(email=data['email']).first()
        if not user:
            response = {
                'status': 'error',
                'message': 'User not found'
            }
            return HTTPResponse(response, 400)
        user.first_name = data['first_name']
        user.last_name = data['last_name']
        user.save()
        response = {
            'status': 'success',
            'message': 'Profile updated successfully'
        }
        return HTTPResponse(response, 400)
    except:
        response = {
            'status': 'error',
            'message': "Error while updating profile",
        }
        return HTTPResponse(response, 400)
