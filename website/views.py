from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request,'iGurd/index.html',{})

def contact(request):
    return render(request, 'iGurd/index.html', {})

def dashboard(request):
    pass

def editac(request):
    pass

def cashcalculator(request):
    pass

def inside_escrow(request):
    pass

def join_as_partner(request):
    pass

def login(request):
    pass

def privacy(request):
    pass

def restore_password(request):
    pass

def signup(request):
    pass

def phone_otp(request):
    pass

def toc(request):
    pass