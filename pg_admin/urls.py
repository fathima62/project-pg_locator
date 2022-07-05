from django.urls import path

from . import views

app_name='pgadmin'

urlpatterns=[
    path('login',views.login,name="adminlogin"),
    path('logout',views.logout,name="adminlogout"),
    
]