from django.views.decorators.http import require_http_methods
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.core.mail import send_mail
import json
from django.http import HttpResponse
from django.core.exceptions import ValidationError
from ..serializer import ProductSerializer, UserSerializer
from ..models import Product
from ..utils import generate_otp, send_email, HTTPResponse, is_otp_valid
from datetime import datetime, timedelta


@require_http_methods(["GET"])
@csrf_exempt
def get_products(request):
    try:
        products = Product.objects.all()
        response = {
            'status': 'success',
            'data': ProductSerializer(products, many=True).data
        }
        return HTTPResponse(response, 200)
    except Exception as e:
        response = {
            'status': 'error',
            'message': f"Error while getting products {str(e)} Try again later",
        }
        return HTTPResponse(response, 500)


@require_http_methods(["GET"])
@csrf_exempt
def get_product(request, id):
    try:
        product = Product.objects.filter(id=id).first()
        if not product:
            response = {
                'status': 'error',
                'message': 'Product not found'
            }
            return HTTPResponse(response, 400)
        response = {
            'status': 'success',
            'data': ProductSerializer(product).data
        }
        return HTTPResponse(response, 200)
    except:
        response = {
            'status': 'error',
            'message': f"Error while getting product!",
        }
        return HTTPResponse(response, 500)
