from django.urls import path
from views import tenders_list


urlpatterns = [
    path('tender/', tenders_list),
]