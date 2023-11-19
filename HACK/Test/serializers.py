from django.contrib.auth.models import Group
from rest_framework import serializers
from .models import User, Form


class FormSerializer(serializers.ModelSerializer):
    class Meta:
        model = Form
        fields = ["name", "factory", "Change", "data", "duration", "team", "message", "incident", "status"]

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["name", "password"]
