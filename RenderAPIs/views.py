from django.shortcuts import render
from django.http import HttpResponse
from RenderAPIs import authenticate

def index(request):
    auth = authenticate.AuthAPI()
    bodyString = auth.createBodyString()  
    pageRender = auth.render(bodyString)  
    return HttpResponse(pageRender)

