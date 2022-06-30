from turtle import title
from django.db import models
from django .utils import  timezone
import datetime
from django.contrib.auth.models import User


class Bidder(models.Model):
    # user model 1:1
    # user = models.OneToOneField(User, on_delete=models.CASCADE)
    # name = models.CharField(max_length=200)
    # phone = models.CharField(max_length=100)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name

class Tenderer(models.Model):
    # user model 1:1
    # user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    # name = models.CharField(max_length=200)
    # phone = models.CharField(max_length=100)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name

class Tenders(models.Model):
    tenderer = models.ForeignKey(Tenderer, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    pdf_tender = models.FileField(upload_to='pdf_tender/', null=True)
    created_at = models.DateTimeField(default=timezone.now, null=True)
    updated_at = models.DateTimeField(default=timezone.now, null=True)
    phone = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    # endate = models.DateTimeField(default=timezone.now)
    insurance_money = models.CharField(max_length=100, default=0)
    terms_of_ref_price = models.CharField(max_length=100, default=0)

    def __str__(self):
        return self.title


class Bid(models.Model):
    # title = models.CharField(max_length=100, default='')
    # tenderer = models.ForeignKey(Tenderer, on_delete=models.CASCADE)
    # bidder = models.ForeignKey(Bidder, on_delete=models.CASCADE)
    # tender = models.ForeignKey(Tenders, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)
    pdf_tech = models.FileField(upload_to='pdf_tech/')
    pdf_money = models.FileField(upload_to='pdf_money/')    

    def __str__(self):
        return self.bid_amount


class Mydeals_List_tenderer(models.Model):
    tenderer = models.ForeignKey(Tenderer, on_delete=models.CASCADE)
    tender = models.ForeignKey(Tenders, on_delete=models.CASCADE)
    # bid = models.ForeignKey(Bid, on_delete=models.CASCADE)
    # Date=datetime.datetime.today()

    # class Meta:
    #     ordering = ['Date']
    # def __str__(self):
    #     return self.Date


class Mydeals_List_bidder(models.Model):
    bidder = models.ForeignKey(Bidder, on_delete=models.CASCADE)
    tender = models.ForeignKey(Tenders, on_delete=models.CASCADE)
    # bid = models.ForeignKey(Bid, on_delete=models.CASCADE)
    # Date=datetime.datetime.today()

    # class Meta:
    #     ordering = ['Date']
    # def __str__(self):
    #     return self.Date

## many to many relationship between bidder and tenders
class subscription:
    def __init__(self, tenderer, tender):
        self.tender = tender
        self.tenderer = tenderer
        self.bidder = Bidder.objects.get(user=tenderer)
        self.tenderer = Tenderer.objects.get(user=tender)
        self.bid = Bid.objects.get(tender=tender, tenderer=tenderer)
        self.tender = Tenders.objects.get(tenderer=tenderer, tender=tender)
        