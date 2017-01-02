from django.http import HttpResponse, Http404
from django.template import loader
from django.shortcuts import render
from .forms import ContactoForm
from .models import mensaje
from django.core.mail import send_mail
from django.utils import timezone
#from django.db import connection
#import json

def index(request):
    template = loader.get_template('index.html')
    context = {}
    return HttpResponse(template.render(context, request))

def doctrina(request):
    template = loader.get_template('doctrina.html')
    context = {}
    return HttpResponse(template.render(context, request))

def nosotros(request):
    template = loader.get_template('nosotros.html')
    context = {}
    return HttpResponse(template.render(context, request))

def contacto(request):
    #send_mail("pagina web", "hola ","michellemuroya96@gmail.com" ,["michelle_muroya@hotmail.com"] )

        # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = ContactoForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            m = mensaje(nombres = form.cleaned_data['nombre'], apellidos = form.cleaned_data['apellidos'], num_proveedor = form.cleaned_data['number'], correo = form.cleaned_data['email'], dia = timezone.now(),departamento = form.cleaned_data['departamento'], provincia = form.cleaned_data['provincia'], mensaje = form.cleaned_data['mensaje'])
            m.save()
            return index(request)
        else:
            print "form not valid"
    # if a GET (or any other method) we'll create a blank form
    else:
        print "form is not valid"
        form = ContactoForm()

    return render(request, 'contacto.html', {'form': form})
    #template = loader.get_template('contacto.html')
    #return HttpResponse(template.render({},request))

def error(request):
    template = loader.get_template('404error.html');
    return HttpResponse(template.render({},request))
