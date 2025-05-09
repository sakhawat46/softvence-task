from rest_framework import serializers
from .models import Employer

class EmployerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employer
        fields = '__all__'
        read_only_fields = ('user', 'created_at')

    def validate_email(self, value):
        if not value:
            raise serializers.ValidationError("Email is required")
        return value

    def validate_phone_number(self, value):
        if not value:
            raise serializers.ValidationError("Phone number is required")
        return value