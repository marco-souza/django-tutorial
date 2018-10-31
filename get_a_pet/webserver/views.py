# from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(req):
    return HttpResponse("<b>Hello World. You're the webserver index</b>")
    # return render(req, "<b>Hello World. You're the webserver index</b>",)
