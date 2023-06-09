from rest_framework import serializers
from django.contrib.auth import get_user_model

class UserSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)
    
    class Meta:
        model = get_user_model()
        fields = ['username', 'password', 'password2', 'email', 'first_name', 'last_name', 'image', 'job']
        extra_kwargs = {
            'password': {'write_only': True},
        }

    def validate(self, data):
        if 'password' in data and data['password'] != data['password2']:
            raise serializers.ValidationError("Passwords must match.")
        return data


    def create(self, validated_data):
        image = validated_data.pop('image', None)
        validated_data.pop('password2')
        user = get_user_model().objects.create_user(**validated_data)
        if image:
            user.image = image
            user.save()
        return user
    
    def update(self, instance, validated_data):
        password = validated_data.pop('password', None)
        instance = super().update(instance, validated_data)
        if password:
            instance.set_password(password)
            instance.save()
        return instance