from django.shortcuts import render
from django.http import HttpResponse
from RenderAPIs import authenticate
from django.http import HttpResponseRedirect
from RenderAPIs import forms


def index(request):    
    # if this is a POST request we need to process the form data
    submitbutton= request.POST.get("submit")
    key = ""
    token = ""
    
    # create a form instance and populate it with data from the request:
    form = forms.InputForm(request.POST)        
        # check whether it's valid:
    if form.is_valid():
        # process the data in form.cleaned_data as required
        # ...
        key = form.cleaned_data.get("api_key")
        token = form.cleaned_data.get("api_token")                     
        
        auth = authenticate.AuthAPI()
        bodyString = auth.createBodyString(key, token)  
        pageRender = auth.render(bodyString) 
        return HttpResponse(pageRender)
        
    # if a GET (or any other method) we'll create a blank form
    else:
        form = forms.InputForm()

    context= {'form': form, 'api_key': key, 'api_token':token,'submitbutton': submitbutton}
    return render(request, 'main_page.html', context)

def thanks(request):
    return HttpResponse("Thank you for your input")

    


    
