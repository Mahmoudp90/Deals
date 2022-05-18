from dataclasses import fields
from pyexpat import model
from rest_framework import serializers
from api.models import Bidder, Bidderslist, Tenderer, Tenders, mydeals_bidder, mydeals_tenderer
from models import models





class tendererserializers(serializers.ModelSerializer):
    class Meta:
        model = Tenderer
        fields = '__all__'


class tendersserializers(serializers.ModelSerializer):
    class Meta:
        model = Tenders
        fields = '__all__'


class bidderserializers(serializers.ModelSerializer):
    class Meta:
        model = Bidder
        fields = '__all__'



class bidderslistserializers(serializers.ModelSerializer):
    class Meta:
        model = Bidderslist
        fields = '__all__'


class mydeals_tendererserializers(serializers.ModelSerializer):
    class Meta:
        model = mydeals_tenderer
        fields = '__all__'


class mydeals_bidderserializer(serializers.ModelSerializer):
    class Meta:
        model = mydeals_bidder
        fields = '__all__'        


