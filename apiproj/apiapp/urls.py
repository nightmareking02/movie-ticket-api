from django.urls import path
from apiapp import views
from django.conf.urls.static import static
from django.conf import settings
from apiapp.views import createmodel

urlpatterns=[
    path('',views.trainapi,name="trainapi"),   
    path('<int:id>/',views.trainapi), 
    path('savefile/',views.savefile), 
    path('create',views.createmodel.as_view(),name='create'),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
