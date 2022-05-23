from django.urls import path
from .views import tenders_list, tenderers_list, bids_list, mydeals_list, CustomAuthToken


urlpatterns = [
    path('tender/', tenders_list),
    path('tender/<int:pk>/', tenders_list),
    path('auth',CustomAuthToken.as_view()),
    path('tenderer/', tenderers_list),
    path('tenderer/<int:pk>/', tenderers_list),
    path('bid/', bids_list),
    path('bid/<int:pk>/', bids_list),
    path('mydeals/', mydeals_list),
    path('mydeals/<int:pk>/', mydeals_list),
]