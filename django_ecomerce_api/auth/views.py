# from django.shortcuts import render
# from django.views.decorators.csrf import csrf_exempt
# from django.http import HttpResponse
# from django.core.mail import send_mail
# from django.http import JsonResponse
# import json

# from .models import Customer
# # send_mail(
# #     "Subject here",
# #     "Here is the message.",
# #     "from@example.com",
# #     ["to@example.com"],
# #     fail_silently=False,
# # )


# def index(request):
#     return HttpResponse("Auth app index page")


# @csrf_exempt
# def login(request):
#     if request.method == "POST":
#         # Login logic
#         return HttpResponse("Login successful")


# @csrf_exempt
# def register(request):
#     if request.method == "POST":
#         try:
#             data = json.loads(request.body)
#             user = Customer.objects.create(
#                 email=data['username'], password=data['password'])
#             print(user)
#             if user:
#                 response = {
#                     'status': 'success',
#                     'message': 'User registered successfully',
#                     'data': user
#                 }
#         except json.JSONDecodeError:
#             response = {
#                 'status': 'error',
#                 'message': 'Invalid JSON data'
#             }
#     else:
#         response = {
#             'status': 'error',
#             'message': 'Only POST requests are allowed'
#         }
#         return httpResponse(response, status=400)

#     return JsonResponse(response).status_code(201)
#     # return HttpResponse(JsonResponse(response), status=201, reason="Created", content_type="application/json")


# @csrf_exempt
# def logout(request):
#     return HttpResponse("Logout successful")


# @csrf_exempt
# def forgot_password(request):
#     return HttpResponse("Forgot password successful")


# @csrf_exempt
# def verify_email(request):
#     return HttpResponse("Verify email successful")


# @csrf_exempt
# def confirm_reset_password(request):
#     return HttpResponse("Confirm reset password successful")


# @csrf_exempt
# def reset_password(request):
#     return HttpResponse("Reset password successful")


# @csrf_exempt
# def change_password(request):
#     return HttpResponse("Change password successful")


# @csrf_exempt
# def update_profile(request):
#     return HttpResponse("Update profile successful")
