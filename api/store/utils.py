# Utils file is used to store utility functions that can be used across the project.

from datetime import datetime
import json
from django.http import HttpResponse, HttpResponseRedirect
from django.core.mail import BadHeaderError, send_mail
from django.http import HttpResponse
from django.http import JsonResponse
import random
import string
import time
from django.utils import timezone
import jwt
from dotenv import dotenv_values
config = dotenv_values(".env")

# class Response(object):
#     def __init__(self, status, message, data):
#         self.status = status
#         self.message = message
#         self.data = data

#     def to_json(self):
#         return json.dumps(self.__dict__)


# def validate_json_data(data):
#     try:
#         json.loads(data)
#         return True
#     except ValueError:
#         return False

def HTTPResponse(response, status_code):
    return HttpResponse(JsonResponse(response), status=status_code, content_type="application/json")


def send_email(subject, message, from_email, to):
    if subject and message and to:
        try:
            send_mail(
                subject,
                message,
                from_email,
                [to],
                fail_silently=False,
            )
        except:
            raise Exception("Email sending failed.")


def generate_otp(length=4):
    """Generate a random OTP.
    Args:
        length (int, optional): The length of the OTP. Defaults to 4.
    Returns:
        str: The generated OTP.
    """
    otp = ""
    for i in range(length):
        otp += random.choice(string.digits)
        # otp += str(random.randint(0, 9))
    return otp


def is_otp_valid(otp_input, otp_storage, expire_at):
    """
    Vérifie si l'OTP fourni est valide et n'a pas expiré.

    :param otp_input: L'OTP saisi par l'utilisateur.
    :param otp_storage: Un dictionnaire contenant l'OTP stocké et sa date d'expiration.
    :param expire_at: La date d'expiration de l'OTP.
    :return: True si l'OTP est valide et non expiré, False sinon.
    """
    # current_time = datetime.now()
    current_time = timezone.now()

    # Vérifier si l'OTP correspond et si la date d'expiration n'est pas passée
    if otp_input == otp_storage and current_time <= expire_at:
        return True
    else:
        return False



def checkToken (token):
    try:
        decoded = jwt.decode(token, config['JWT_SECRET'], algorithms=['HS256'])
        return decoded
    except jwt.ExpiredSignatureError:
        return None
