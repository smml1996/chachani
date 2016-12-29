from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^carne/', views.carne, name="carne"),
    url(r'^establos/', views.establos, name="establos"),
    url(r'^fertilizantes/', views.fertiliza, name="fertilizantes"),
    url(r'^forraje/', views.forraje, name="forraje"),
    url(r'^innova/', views.innova, name="innova"),
    url(r'^libros/', views.libros, name="libros"),
    url(r'^premezclas/', views.premezclas, name="premezclas"),
    url(r'^revistas/', views.revistas, name="revistas"),
    url(r'^revista/', views.revista, name="revista"),

]
