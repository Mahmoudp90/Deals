from pyexpat import model
from django import forms
from .models import Bidder, Tenderer, models

class upload_tenderer(forms.ModelForm):
    class Meta:
        model =Tenderer
        fields= 'pdf_terms_of_reference,pdf_primary_insurance'



class upload_bidder(forms.ModelForm):
    class Meta:
        model =Bidder
        fields= 'pdf_terms_of_reference,pdf_primary_insurance'        
        a