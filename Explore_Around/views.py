from django.http import HttpResponse
from django.urls import reverse
from django.shortcuts import HttpResponseRedirect


def index(request):
    
    return HttpResponseRedirect(reverse('Blog_Management_App:blogs'))