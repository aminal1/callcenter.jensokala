from rest_framework import serializers
from users_app.models import UserAccount

class UserSerializer (serializers.ModelSerializer):
    class Meta:
        model = UserAccount
        fields  = ["id","firstname","lastname","phone_number","user_type","is_active"]