from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def post_create(request):
    context = {
        "title": "Create"
    }
    return render(request, "index.html", context)

def post_detail(request):
    context = {
        "title": "Detail"
    }
    return render(request, "index.html", context)

def post_list(request):
    context = {
        "title":"List"
    }
    return render(request,"index.html",context)
    #return HttpResponse("<h1>List</h1>")

def post_update(request):
    context = {
        "title": "Update"
    }
    return render(request, "index.html", context)

def post_delete(request):
    context = {
        "title": "Delete"
    }
    return render(request, "index.html", context)

