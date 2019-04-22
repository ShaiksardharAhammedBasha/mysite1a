from django.urls import path

from facebook import views

urlpatterns = [

		path('', views.index, name='index'),



]