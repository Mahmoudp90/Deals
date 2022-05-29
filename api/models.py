from django.db import models
from django .utils import  timezone
import datetime


class Bidder(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    # pdf_money = models.FileField(upload_to='pdf_money/')
    # pdf_tech = models.FileField(upload_to='pdf_tech/')
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name

# class Bidder(models.Model):
#     username = models.CharField(max_length=100)
#     password = models.CharField(max_length=100)
#     email = models.CharField(max_length=100)
#     phone = models.CharField(max_length=100)
#     # pdf_terms_of_reference = models.FileField(upload_to='terms of reference/pdfs/', default=True)
#     # pdf_primary_insurance = models.FileField(upload_to='terms of primary insurance/pdfs/', default=True)


#     def __str__(self):
#         return self.username


class Tenderer(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    # pdf_terms_of_reference = models.FileField(upload_to='pdf_terms_of_reference/')
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name

# class Tenderer(models.Model):

#     name = models.CharField(max_length=100)
#     password = models.CharField(max_length=100)
#     email = models.CharField(max_length=100)
#     phone = models.CharField(max_length=100)
#     # pdf_terms_of_reference = models.FileField(upload_to='terms of reference/pdfs/', default=True)

#     def __str__(self):
#         return self.name

class Tenders(models.Model):
    tenderer = models.ForeignKey(Tenderer, on_delete=models.CASCADE)
    # bidder = models.ForeignKey(Bidder, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    pdf_tender = models.FileField(upload_to='pdf_tender/')
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)
    phone = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    endate = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

# class Tenders(models.Model):
#     title = models.CharField(max_length=100)
#     tenderername = models.CharField(max_length=100)
#     email = models.EmailField(max_length=100)
#     # startdate = datetime.date.today()
#     activate =models.BooleanField(default=True)
#     tenderer = models.ForeignKey(Tenderer, on_delete=models.CASCADE)
#     Bidder = models.ForeignKey(Bidder, on_delete=models.CASCADE, default="")
#     enddate = models.CharField(max_length=100 )
#     phone = models.CharField(max_length=20)
#     address = models.CharField(max_length=100)
#     terms_of_reference=models.CharField(max_length=100)
#     primary_insurance=models.CharField(max_length=100)


 
    # def  active(self,Tenders):
    #     activate=True
    #     date =datetime.date().today()
    #     if date > datetime.date.today:
    #         activate=False

       
class Bid(models.Model):
    tenderer = models.ForeignKey(Tenderer, on_delete=models.CASCADE)
    bidder = models.ForeignKey(Bidder, on_delete=models.CASCADE)
    tender = models.ForeignKey(Tenders, on_delete=models.CASCADE)
    # bid_amount = models.CharField(max_length=100)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)
    pdf_tech = models.FileField(upload_to='pdf_tech/')
    pdf_money = models.FileField(upload_to='pdf_money/')    

    def __str__(self):
        return self.bid_amount


# class Bidders_List(models.Model):
#      Bidder = models.ManyToManyField(Bidder)
    #  Date=datetime.datetime.today()

    #  class Meta:
    #      ordering = ['Date']
    #  def __str__(self):
    #     return self.Date

class Mydeals_List(models.Model):
    tenderer = models.ForeignKey(Tenderer, on_delete=models.CASCADE)
    tender = models.ForeignKey(Tenders, on_delete=models.CASCADE)
    bid = models.ForeignKey(Bid, on_delete=models.CASCADE)
    # Date=datetime.datetime.today()

    # class Meta:
    #     ordering = ['Date']
    # def __str__(self):
    #     return self.Date


# class Mydeals_Tenderer(models.Model):
#     tenderer = models.ForeignKey(Tenderer, on_delete=models.CASCADE)
#     #Tenders = models.ManyToOneRel(Tenders,)


# class Mydeals_Bidder(models.Model):
#     bidder = models.ForeignKey(Bidder, on_delete=models.CASCADE)
#     #Tenders= models.ManyToManyRel(Tenders)    


# Token model for user authentication 
# class Token(models.Model):
#     user = models.OneToOneField(Bidder or Tenderer, on_delete=models.CASCADE)
#     token = models.CharField(max_length=255)

#     def __str__(self):
#         return self.token