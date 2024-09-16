from django.views.decorators.http import require_http_methods
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.core.mail import send_mail
import json
from django.http import HttpResponse
from django.core.exceptions import ValidationError
from ..serializer import UserSerializer
from ..models import Customer
from ..utils import generate_otp, send_email, HTTPResponse, is_otp_valid
from datetime import datetime, timedelta


@require_http_methods(["GET"])
@csrf_exempt
def get_orders(request):
    return HttpResponse("Update profile successful")


@require_http_methods(["POST"])
@csrf_exempt
def create_order(request):
    return HttpResponse("Update profile successful")
