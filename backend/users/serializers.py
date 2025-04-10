from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password
from .models import User, UserActivity

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'role',
                  'first_name', 'last_name', 'is_active', 'date_joined']
        read_only_fields = ['date_joined']


class UserCreateSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ('username', 'password', 'password2',
                  'email', 'role', 'first_name', 'last_name')

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError(
                {"password": "Password fields didn't match."})
        return attrs

    def create(self, validated_data):
        validated_data.pop('password2')
        user = User.objects.create_user(**validated_data)
        return user


class UserUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name', 'role')


class UserActivitySerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    action_type_display = serializers.CharField(
        source='get_action_type_display', read_only=True)

    class Meta:
        model = UserActivity
        fields = ['id', 'user', 'action_type', 'action_type_display',
                  'model_name', 'object_id', 'details', 'ip_address', 'created_at']
        read_only_fields = ['user', 'action_type', 'model_name',
                            'object_id', 'details', 'ip_address', 'created_at']
