import imp
from multiprocessing.spawn import import_main_path
from pkgutil import ImpImporter
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.views import APIView
from rest_framework import status, generics, mixins, permissions
from .models import Bidder, Tenderer, Mydeals_List_tenderer,Mydeals_List_bidder, Bid, Tenders
from .serializers import BidSerializer, Tenders_Serializers, BidderSerializer, Mydeals_List_bidderSerializer,Mydeals_List_tendererSerializer, TendererSerializer


# Create your views here


# Generic Apiview with mixin class for tenders
class Tenders_Detail(generics.GenericAPIView, mixins.CreateModelMixin, mixins.ListModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, mixins.RetrieveModelMixin):
    serializer_class = Tenders_Serializers
    queryset = Tenders.objects.all()
    lookup_field = 'id'
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [TokenAuthentication]

    def get(self, request, id=None):
        if id:
            return self.retrieve(request)
        else:
            return self.list(request)

    def post(self, request):
        return self.create(request)

    def put(self, request, id=None):
        return self.update(request, id)

    def delete(self, request, id):
        return self.destroy(request, id)

# Generic Apiview with mixin class for bidder
class Bidder_Detail(generics.GenericAPIView, mixins.CreateModelMixin, mixins.ListModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, mixins.RetrieveModelMixin):
    serializer_class = BidderSerializer
    queryset = Bidder.objects.all()
    lookup_field = 'id'
    # permission_classes = [permissions.IsAuthenticated]
    # authentication_classes = [TokenAuthentication]

    def get(self, request, id=None):
        if id:
            return self.retrieve(request)
        else:
            return self.list(request)

    def post(self, request):
        return self.create(request)

    def put(self, request, id=None):
        return self.update(request, id)

    def delete(self, request, id):
        return self.destroy(request, id)

# Generic Apiview with mixin class for tenderer
class Tenderer_Detail(generics.GenericAPIView, mixins.CreateModelMixin, mixins.ListModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, mixins.RetrieveModelMixin):
    serializer_class = TendererSerializer
    queryset = Tenderer.objects.all()
    lookup_field = 'id'
    # permission_classes = [permissions.IsAuthenticated]
    # authentication_classes = [TokenAuthentication]

    def get(self, request, id=None):
        if id:
            return self.retrieve(request)
        else:
            return self.list(request)

    def post(self, request):
        return self.create(request)

    def put(self, request, id=None):
        return self.update(request, id)

    def delete(self, request, id):
        return self.destroy(request, id)

# Generic Apiview with mixin class for mydeals_list_tenderer
class Mydeals_List_tenderer_Detail(generics.GenericAPIView, mixins.CreateModelMixin, mixins.ListModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, mixins.RetrieveModelMixin):
    serializer_class = Mydeals_List_tendererSerializer
    queryset = Mydeals_List_tenderer.objects.all()
    lookup_field = 'id'
    # permission_classes = [permissions.IsAuthenticated]
    # authentication_classes = [TokenAuthentication]

    def get(self, request, id=None):
        if id:
            return self.retrieve(request)
        else:
            return self.list(request)

    def post(self, request):
        return self.create(request)

    def put(self, request, id=None):
        return self.update(request, id)

    def delete(self, request, id):
        return self.destroy(request, id)


# Generic Apiview with mixin class for mydeals_list_bidder
class Mydeals_List_bidder_Detail(generics.GenericAPIView, mixins.CreateModelMixin, mixins.ListModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, mixins.RetrieveModelMixin):
    serializer_class = Mydeals_List_bidderSerializer
    queryset = Mydeals_List_bidder.objects.all()
    lookup_field = 'id'
    # permission_classes = [permissions.IsAuthenticated]
    # authentication_classes = [TokenAuthentication]

    def get(self, request, id=None):
        if id:
            return self.retrieve(request)
        else:
            return self.list(request)

    def post(self, request):
        return self.create(request)

    def put(self, request, id=None):
        return self.update(request, id)

    def delete(self, request, id):
        return self.destroy(request, id)



# Generic Apiview with mixin class for bid
class Bid_Detail(generics.GenericAPIView, mixins.CreateModelMixin, mixins.ListModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, mixins.RetrieveModelMixin):
    serializer_class = BidSerializer
    queryset = Bid.objects.all()
    lookup_field = 'id'
    # permission_classes = [permissions.IsAuthenticated]
    # authentication_classes = [TokenAuthentication]

    def get(self, request, id=None):
        if id:
            return self.retrieve(request)
        else:
            return self.list(request)

    def post(self, request):
        return self.create(request)

    def put(self, request, id=None):
        return self.update(request, id)

    def delete(self, request, id):
        return self.destroy(request, id)


    

    

# Create apiviews for tenders
# class Tenders_List(APIView):
#     def get(self, request, format=None):
#         tenders = Tenders.objects.all()
#         serializer = Tenders_Serializers(tenders, many=True)
#         return Response(serializer.data)

#     def post(self, request, format=None):
#         serializer = Tenders_Serializers(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



# @api_view(['GET', 'POST'])
# def tenders_list(request):
#     if request.method == 'GET':
#         tenders = Tenders.objects.all()
#         serializer = Tenders_Serializers(tenders, many=True)
#         return Response(serializer.data)

#     elif request.method == 'POST':
#         data = JSONParser().parse(request)
#         serializer = Tenders_Serializers(data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(status=status.HTTP_400_BAD_REQUEST)


# # list all bids
# @api_view(['GET', 'POST'])
# def bids_list(request):
#     if request.method == 'GET':
#         bids = Bid.objects.all()
#         serializer = BidSerializer(bids, many=True)
#         return JsonResponse(serializer.data, safe=False)

#     elif request.method == 'POST':
#         data = JSONParser().parse(request)
#         serializer = BidSerializer(data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data, status=201)
#         return JsonResponse(serializer.errors, status=400)


# # list all tenderers
# @api_view(['GET', 'POST'])
# def tenderers_list(request):
#     if request.method == 'GET':
#         tenderers = Tenderer.objects.all()
#         serializer = TendererSerializer(tenderers, many=True)
#         return JsonResponse(serializer.data, safe=False)

#     elif request.method == 'POST':
#         data = JSONParser().parse(request)
#         serializer = TendererSerializer(data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data, status=201)
#         return JsonResponse(serializer.errors, status=400)


# # return mydeals_list
# @api_view(['GET'])
# def mydeals_list(request):
#     if request.method == 'GET':
#         mydeals_list = Mydeals_List.objects.all()
#         serializer = Mydeals_ListSerializer(mydeals_list, many=True)
#         return JsonResponse(serializer.data, safe=False)


# # Token authentication for bidder and tenderer
# class CustomAuthToken(ObtainAuthToken):
#     def post(self, request, *args, **kwargs):
#         serializer = AuthTokenSerializer(data=request.data, context={'request': request})
#         serializer.is_valid(raise_exception=True)
#         user = serializer.validated_data['user']
#         token, created = Token.objects.get_or_create(user=user)
#         return Response({
#             'token': token.key,
#             'user_id': user.pk,
#             'email': user.email
#         })


