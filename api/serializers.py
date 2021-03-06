from dataclasses import fields
import email
from pyexpat import model
from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from rest_framework.validators import UniqueValidator, UniqueTogetherValidator
from .models import Bidder, Tenderer, Mydeals_List_bidder, Mydeals_List_tenderer, Bid, Tenders


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = (
            'id',
            'username',
            'first_name',
            'last_name',
            'email',
            'password',
        )
        validators = [
            UniqueTogetherValidator(
                queryset=User.objects.all(),
                fields=['username', 'email'],
                message= 'Username and email must be unique together.'
            )
        ]
    
    # create user
    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

    # update password
    def update(self, instance, validated_data):
        password = validated_data.pop('password', None)
        user = super().update(instance, validated_data)
        if password:
            user.set_password(password)
            user.save()
        return user

    # change user email
    def update_email(self, instance, validated_data):
        user = super().update(instance, validated_data)
        user.email = validated_data.pop('email')
        user.save()
        return user

class Tenders_Serializers(ModelSerializer):
    class Meta:
        model = Tenders
        fields = '__all__'


class TendererSerializer(ModelSerializer):
    class Meta:
        model = Tenderer
        fields = '__all__'

class BidderSerializer(ModelSerializer):
    class Meta:
        model = Bidder
        fields = '__all__'


class Mydeals_List_tendererSerializer(ModelSerializer):
    class Meta:
        model = Mydeals_List_tenderer
        fields = '__all__'


class Mydeals_List_bidderSerializer(ModelSerializer):
    class Meta:
        model = Mydeals_List_bidder
        fields = '__all__'


class BidSerializer(ModelSerializer):
    class Meta:
        model = Bid
        fields = '__all__'


class ChangePasswordSerializer(serializers.Serializer):
    model = User

    """
    Serializer for password change endpoint.
    """
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)



