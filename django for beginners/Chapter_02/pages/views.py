from django.shortcuts import render
from django.http import HttpResponse


'''
it`s a function correspond to the main page
'''
def home_page_view(request):
    return HttpResponse('Hello, World!')