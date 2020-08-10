from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, 'iGurd/index.html', {})


def contact(request):
    return render(request, 'iGurd/innerPages/contact.html', {})


def dashboard(request):
    return render(request, 'iGurd/innerPages/Dashboard.html', {})


def edit_ac(request):
    return render(request, 'iGurd/innerPages/edit-account.html', {})


def cash_calculator(request):
    return render(request, 'iGurd/innerPages/fee-calculator.html', {})


def inside_escrow(request):
    return render(request, 'iGurd/innerPages/insideEscrow.html', {})


def join_as_partner(request):
    return render(request, 'iGurd/innerPages/join-as-a-partner.html', {})


def login(request):
    return render(request, 'iGurd/innerPages/login.html', {})


def privacy(request):
    return render(request, 'iGurd/innerPages/privacy.html', {})


def restore_password(request):
    return render(request, 'iGurd/innerPages/restorePassword.html', {})


def signup(request):
    return render(request, 'iGurd/innerPages/signup.html', {})


def phone_otp(request):
    return render(request, 'iGurd/innerPages/signup2.html', {})


def toc(request):
    return render(request, 'iGurd/innerPages/toc.html', {})
