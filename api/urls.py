from django.urls import path
# from .views import tenders_list, tenderers_list, bids_list, mydeals_list, CustomAuthToken
from .views import Tenders_Detail, Bidder_Detail, Tenderer_Detail, Mydeals_List_Detail, Bid_Detail 


urlpatterns = [
    # path('tender/', tenders_list),
    # path('tender/<int:pk>/', tenders_list),
    # path('auth',CustomAuthToken.as_view()),
    # path('tenderer/', tenderers_list),
    # path('tenderer/<int:pk>/', tenderers_list),
    # path('bid/', bids_list),
    # path('bid/<int:pk>/', bids_list),
    # path('mydeals/', mydeals_list),
    # path('mydeals/<int:pk>/', mydeals_list),
    path('tender/', Tenders_Detail.as_view()),
    path('tender/<int:id>/', Tenders_Detail.as_view()),
    path('bidder/<int:id>/', Bidder_Detail.as_view()),
    path('bidder/', Bidder_Detail.as_view()),
    path('tenderer/<int:id>/', Tenderer_Detail.as_view()),
    path('tenderer/', Tenderer_Detail.as_view()),
    path('mydeals/<int:id>/', Mydeals_List_Detail.as_view()),
    path('mydeals/', Mydeals_List_Detail.as_view()),
    path('bid/<int:id>/', Bid_Detail.as_view()),
    path('bid/', Bid_Detail.as_view()),

]