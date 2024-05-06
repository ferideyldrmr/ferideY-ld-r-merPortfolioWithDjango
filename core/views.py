from django.shortcuts import render
from django.core.mail import send_mail

def index(request):
    return render(request, 'index.html')
def contact(request):
    return render(request, 'index.html')
