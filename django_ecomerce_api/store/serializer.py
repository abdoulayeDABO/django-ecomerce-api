# Serializer is used to serialize the data from the model to JSON format and vice versa.
# It also validates the data before saving it to the database. The serializer is used in the views to create, update, and delete data from the database.
from rest_framework import serializers

from .models import Product


class UserSerializer(serializers.Serializer):
    """Serializer class to serialize and deserialize data from the model to JSON format and vice versa."""

    email = serializers.EmailField()
    password = serializers.CharField(max_length=128)
    first_name = serializers.CharField(max_length=128)
    last_name = serializers.CharField(max_length=128)
    phone = serializers.CharField(max_length=128)
    address = serializers.CharField(max_length=128)
    city = serializers.CharField(max_length=128)
    state = serializers.CharField(max_length=128)
    country = serializers.CharField(max_length=128)
    role = serializers.CharField(max_length=128)
    created_at = serializers.DateField()
    updated_at = serializers.DateField()
    is_confirmed = serializers.BooleanField()
    otp = serializers.CharField(max_length=4)
    otp_expires_at = serializers.DateTimeField()

    # def create(self, validated_data):
    #     """Create a new user."""
    #     return Customer.objects.create(**validated_data)

    # def update(self, instance, validated_data):
    #     """Update an existing user."""
    #     for key, value in validated_data.items():
    #         setattr(instance, key, value)
    #     instance.save()
    #     return instance


# class ProductSerializer(serializers.Serializer):
#     name = serializers.CharField(max_length=255)
#     description = serializers.CharField(max_length=255)
#     price = serializers.FloatField()
#     category = serializers.CharField(max_length=255)
#     in_stock = serializers.BooleanField(default=True)
#     image = serializers.CharField()
#     created_at = serializers.DateTimeField()
#     image_url = serializers.CharField()

class ProductSerializer(serializers.ModelSerializer):

    image_url = serializers.SerializerMethodField('get_image_url')

    class Meta:
        model = Product
        fields = '__all__'

    def get_image_url(self, obj):
        return "http://localhost:8000/static/" + str(obj.image)

# class AccountSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Account
#         fields = '__all__'

# class AccountSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Account
#         exclude = ['users']
