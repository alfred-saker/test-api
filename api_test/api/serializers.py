from rest_framework import serializers

class RegistrationSerializer(serializers.Serializer):
  email = serializers.EmailField()
  password1 = serializers.CharField(write_only=True)
  password2 = serializers.CharField(write_only=True)