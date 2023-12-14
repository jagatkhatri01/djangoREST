from rest_framework import serializers
from .models import Person, Address
from django.contrib.auth.models import User



import re

class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

class RegisterSerializer(serializers.Serializer):
    username = serializers.CharField()
    email = serializers.EmailField()
    password = serializers.CharField()

    def validate(self, data):
        if data['username']:
            if User.objects.filter(username=data['username']).exists():
                raise serializers.ValidationError("Username already exists")
            
        if data['email']:
            if User.objects.filter(email=data['email']).exists():
                raise serializers.ValidationError("Email already exists")
        print(data)
        return data
    
    def create(self, validated_data):
        user = User.objects.create(username=validated_data['username'], email = validated_data['email'])
        user.set_password(validated_data['password'])
        print(validated_data)
        return validated_data

   
class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = ['city']
class PeopleSerializer(serializers.ModelSerializer):
    address = AddressSerializer()
    class Meta:
        model = Person
        fields = '__all__'
        # depth = 1

    def validate(self, data):
        age = data.get('age')
        first_name = data.get('first_name')
        last_name = data.get('last_name')

        if age is not None and age < 18:
            raise serializers.ValidationError("Age must be greater than 18!")

        if first_name is not None and len(first_name) < 3:
            raise serializers.ValidationError("First name must be at least 3 characters long!")

        if last_name is not None and len(last_name) < 3:
            raise serializers.ValidationError("Last name must be at least 3 characters long!")

        if not re.match("^[a-zA-Z0-9]*$", first_name):
            raise serializers.ValidationError("First name cannot include special characters.")
        
        if not re.match("^[a-zA-Z0-9]*$", last_name):
            raise serializers.ValidationError("Last name cannot include special characters.")

        return data

