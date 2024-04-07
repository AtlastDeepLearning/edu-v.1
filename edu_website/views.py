from django.shortcuts import render

def home(request):
    return render(request, 'home.html', {})

def about(request):
    return render(request, 'about.html', {})

def services(request):
    return render(request, 'services.html', {})

def why(request):
    return render(request, 'why.html', {})

def team(request):
    return render(request, 'team.html', {})