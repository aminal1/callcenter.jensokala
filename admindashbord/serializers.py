from rest_framework import serializers
from users_app.models import UserAccount
from .models import Product

class UserSerializer (serializers.ModelSerializer):
    class Meta:
        model = UserAccount
        fields  = ["id","firstname","lastname","phone_number","user_type","is_active"]


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = [
            'refrence_id',
            'title',
            'price',
            'mainImage',
            'code',
        ]