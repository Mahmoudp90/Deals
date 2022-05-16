from django.db import models
from django .utils import  timezone
import datetime


class Tenderer(models.Model):

    name = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Tenders(models.Model):
    title = models.CharField(max_length=100)
    tenderername = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    startdate = datetime.date.today()
    activate =models.BooleanField(default=True)
    tenderer = models.ForeignKey(Tenderer, on_delete=models.CASCADE)
    enddate = models.CharField(max_length=100 )
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=100)
    terms_of_reference=models.CharField(max_length=100)
    primary_insurance=models.CharField(max_length=100)


# def active(self,Tenders):
#     date=datetime.date().today()
#     if date > Tenders.enddate:
#         Tenders.activate= False

class Bidder(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)

    def __str__(self):
        return self.username

# class Bidderslist(models.Model):
#     Bidder = models.ManyToManyField(Bidder)
#     Date=datetime.datetime.today()

#     #class Meta:
#      #   ordering = ['Date']

#     def __str__(self):
#         return self.Date

#class mydeals_tenderer(models.Model):
 #   tenderer = models.ForeignKey(Tenderer, on_delete=models.CASCADE)
  #  Tenders = models.ManyToOneRel()

    