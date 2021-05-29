from django.urls import path

from . import views

urlpatterns = [

    path("snippet_detail", views.snippet_detail, name ='snippet_detail'),
    path("allsnips", views.allsnips, name ='allsnips'),
]
