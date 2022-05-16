import imp
from multiprocessing.spawn import import_main_path
from pkgutil import ImpImporter
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser


def tenders_list(request):
    
