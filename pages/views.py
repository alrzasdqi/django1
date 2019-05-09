from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def home_view(request, *args, **kwargs):
    print(args, kwargs)
    print(request.user)
    #return HttpResponse("<h1>This is My HOME Page!!!</h1>")
    return render(request, "home.html", {})

def contact_view(request, *args, **kwargs):
    return render(request, "contact.html", {})

def about_view(request, *args, **kwargs):
    my_context = {
        "my_text" : "This is about us",
        "This_is_True" : True,
        "my_number" : 123,
        "my_list" : [123, 345, 6666, "ABC"]
    }
    return render(request, "about.html", my_context)

def social_view(request, *args, **kwargs):
    return render(request, "social.html", {})