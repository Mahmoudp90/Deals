import imp
from multiprocessing.spawn import import_main_path
from pkgutil import ImpImporter
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.views import APIView
from rest_framework import status, generics, mixins, permissions
from .models import Bidder, Tenderer, Mydeals_List_tenderer,Mydeals_List_bidder, Bid, Tenders
from .serializers import BidSerializer, Tenders_Serializers, BidderSerializer, UserSerializer
from .serializers import Mydeals_List_bidderSerializer,Mydeals_List_tendererSerializer, TendererSerializer
from rest_framework import generics
from django.contrib.auth.models import User
from .serializers import ChangePasswordSerializer



# Create your views here.


# User Registeration
class register(APIView):
    # permission_classes = [IsAdminUser]

    def get(self, format=None):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid(raise_exception=ValueError):
            serializer.create(validated_data=request.data)
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )
        return Response(
            {
                "error": True,
                "error_msg": serializer.error_messages,
            },
            status=status.HTTP_400_BAD_REQUEST
        )


# Generic Apiview with mixin class for tenders
class Tenders_Detail(generics.GenericAPIView, mixins.CreateModelMixin, mixins.ListModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, mixins.RetrieveModelMixin):
    serializer_class = Tenders_Serializers
    queryset = Tenders.objects.all()
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

class ChangePasswordView(generics.UpdateAPIView):
    """
    An endpoint for changing password.
    """
    serializer_class = ChangePasswordSerializer
    model = User
    permission_classes = (IsAuthenticated,)

    def get_object(self, queryset=None):
        obj = self.request.user
        return obj

    def update(self, request, *args, **kwargs):
        self.object = self.get_object()
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            # Check old password
            if not self.object.check_password(serializer.data.get("old_password")):
                return Response({"old_password": ["Wrong password."]}, status=status.HTTP_400_BAD_REQUEST)
            # set_password also hashes the password that the user will get
            self.object.set_password(serializer.data.get("new_password"))
            self.object.save()
            response = {
                'status': 'success',
                'code': status.HTTP_200_OK,
                'message': 'Password updated successfully',
                'data': []
            }

            return Response(response)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)