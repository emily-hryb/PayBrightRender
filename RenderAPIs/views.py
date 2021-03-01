from django.shortcuts import render
from django.http import HttpResponse
from RenderAPIs import authenticate
from django.http import HttpResponseRedirect
from RenderAPIs import forms


def index(request):
    #auth = authenticate.AuthAPI()
    #bodyString = auth.createBodyString()  
    #pageRender = auth.render(bodyString) 
    return HttpResponse("Main Page. See /input to add info")

def thanks(request):
    return HttpResponse("Thank you for your input")

def get_input(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = forms.InputForm(request.POST)
        # check whether it's valid:
        #if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
        return HttpResponseRedirect('thanks')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = forms.InputForm()

    return render(request, 'main_page.html', {'form': form})