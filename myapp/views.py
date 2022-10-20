from http.client import HTTPResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return HTTPResponse('Welcome!')


def create(request):
    return HTTPResponse('Create')


def read(request, id):
    return HTTPResponse('Read!'+id)