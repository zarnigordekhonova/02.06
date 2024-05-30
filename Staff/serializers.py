from rest_framework import serializers
from .models import Jobs, Company, Workers

class WorkersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Workers
        fields = "__all__"

    def validate_first_name(self, first_name):
        if first_name.isalpha():
            return first_name
        raise serializers.ValidationError({'first_name': 'First name should contain only letters!'})

    def validate_last_name(self, last_name):
        if last_name.isalpha():
            return last_name
        raise serializers.ValidationError({'last_name': 'Last name should contain only letters!'})

    def validate_age(self, age):
        if 14 < age < 50:
            return age
        raise serializers.ValidationError({'age': 'Age must be between 14 and 50!'})

    def validate_username(self, username):
        if len(username) <= 10:
            return username
        raise serializers.ValidationError({'username' : 'Username should contain maximum 10 characters!'})

    def validate_phone_number(self, phone_number):
        if len(phone_number) < 15 and phone_number.startswith('+'):
            return phone_number
        raise serializers.ValidationError({'phone_number' : 'Phone number should contain only numbers up to 15 and start with +!'})

class JobsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Jobs
        fields = "__all__"


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = "__all__"
