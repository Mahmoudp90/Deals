from dataclasses import fields
from pyexpat import model
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from .models import Bidder, Tenderer, Mydeals_List, Bid, Tenders

class Tenders_Serializers(ModelSerializer):
    class Meta:
        model = Tenders
        fields = '__all__'

class BidSerializer(ModelSerializer):
    class Meta:
        model = Bid
        fields = '__all__'


class Mydeals_ListSerializer(ModelSerializer):
    class Meta:
        model = Mydeals_List
        fields = '__all__'


class TendererSerializer(ModelSerializer):
    class Meta:
        model = Tenderer
        fields = '__all__'

class BidderSerializer(ModelSerializer):
    class Meta:
        model = Bidder
        fields = '__all__'

