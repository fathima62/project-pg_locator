from django.urls import path
from . import views

app_name='owner'

urlpatterns=[
    path('login',views.login,name="ownerlogin"),
    path('logout',views.logout,name=
    "ownerlogout")
]