from django.shortcuts import render

# Create your views here.

def login(request):
    return render(request,'owner/login.html')
def logout(request):
    return render(request,'owner/logout.html')
