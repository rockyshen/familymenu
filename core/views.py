from django.shortcuts import render
from django.utils.html import format_html

# Create your views here.

def index(request):
    return render(request, "core/index.html")