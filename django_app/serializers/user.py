import re
from rest_framework import serializers
from django_app.app_configs import app_messages as am
from django_app.app_configs import app_variables as av
from django_app.models.user import UserModel
from app_core.serializers.common_model_serializer import CommonModelSerializer

class UserSerializer(CommonModelSerializer):
    class Meta:
        model = UserModel
        fields = "__all__"
        read_only_fields = ["id", "is_active", "created_at", "updated_at", "deleted_at", "blocked_at"]

    class Options:
        referenced_by = ["profile"]

    password = serializers.CharField(
        write_only=True, 
        required=True, 
        min_length=8, 
        max_length=20
    )

    def validate_password(self, value):
        regex = av.PASSWORD_REGEX
        if not re.search(regex, value):
            raise serializers.ValidationError(am.INVALID_PASSWORD)
        return value

    
    
