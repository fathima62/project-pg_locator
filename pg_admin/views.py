from django.shortcuts import render

# Create your views here.
def login(request):
    return render(request,'pg_admin/login.html')

def logout(request):
    return render(request,'pg_admin/logout.html')
