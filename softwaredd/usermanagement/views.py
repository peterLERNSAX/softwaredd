from django.shortcuts import render, HttpResponse
from django.views import View
from django.http import HttpRequest

# Create your views here.

class IndexView(View):
    """Indexview"""
    def get(self,request:HttpRequest)->HttpResponse:
        """get"""
        return render(request,"usermanagement/index.html")