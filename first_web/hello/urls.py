from django.urls import path
from hello import views

urlpatterns = [
    path("", views.index, name="index"),
    path("scan",views.scan, name="scan"),
    path("createdb",views.createdb, name="createdb"),

]