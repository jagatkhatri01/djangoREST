from rest_framework import serializers
from .models import Person



import re

class PeopleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = '__all__'

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

