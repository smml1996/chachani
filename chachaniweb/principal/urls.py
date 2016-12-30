from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^nosotros/', views.nosotros, name="nosotros"),
    url(r'^contacto/', views.contacto, name="contacto"),
    #url(r'^insertContacto/',views.InsertContacto, name="Insert"),
    url(r'^', views.error),
]
