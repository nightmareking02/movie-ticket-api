from django.urls import path
from movapp import views

urlpatterns=[
    path('movapi/',views.movapi,name="movapi"),
]