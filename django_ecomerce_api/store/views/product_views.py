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
from django.core.paginator import Paginator


@require_http_methods(["GET"])
@csrf_exempt
def get_products(request):
    try:
        print(request.GET)
        products = Product.objects.all()
        paginator = Paginator(products, 5)  # Number of items per page
        page_number = request.GET.get("page")
        page_obj = paginator.get_page(page_number)
        response = {
            'status': 'success',
            'data': ProductSerializer(page_obj, many=True).data,
            'meta': {
                'total': paginator.count,
                'per_page': paginator.per_page,
                'current_page': page_obj.number,
                'has_next': page_obj.has_next(),
                'has_previous': page_obj.has_previous(),
                'next': page_obj.next_page_number(),
                'last': paginator.num_pages,
            }
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
