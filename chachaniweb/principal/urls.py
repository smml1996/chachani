from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^nosotros/', views.nosotros, name="nosotros"),
    url(r'^', views.index, name="index"),

]
