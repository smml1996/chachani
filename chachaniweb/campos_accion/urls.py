from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^alimento/', views.alimento, name="alimento"),
    url(r'^carne/', views.carne, name="carne"),
    url(r'^cultivo/', views.cultivo, name="cultivo"),
    url(r'^establos/', views.establos, name="establos"),
    url(r'^fertilizantes/', views.fertiliza, name="fertilizantes"),
    url(r'^forraje/', views.forraje, name="forraje"),
    url(r'^innova/', views.innova, name="innova"),
    url(r'^libros/', views.libros, name="libros"),
    url(r'^lotes/', views.lotes, name="lotes"),
    url(r'^premezclas/', views.premezclas, name="premezclas"),
    url(r'^revistas/', views.revistas, name="revistas"),
    url(r'^tilapias/', views.tilapias, name="tilapias"),
    url(r'^revista/', views.revista, name="revista"),

]
