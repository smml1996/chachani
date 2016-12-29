from django.http import HttpResponse, Http404
from django.template import loader

def carne(request):
    template = loader.get_template('campos_accion/carne.html')
    context = {}
    return HttpResponse(template.render(context, request))

def establos(request):
    template = loader.get_template('campos_accion/establos.html')
    context = {}
    return HttpResponse(template.render(context, request))

def fertiliza(request):
    template = loader.get_template('campos_accion/fertilizantes.html')
    context = {}
    return HttpResponse(template.render(context, request))

def forraje(request):
    template = loader.get_template('campos_accion/forraje.html')
    context = {}
    return HttpResponse(template.render(context, request))

def innova(request):
    template = loader.get_template('campos_accion/innova.html')
    context = {}
    return HttpResponse(template.render(context, request))

def libros(request):
    template = loader.get_template('campos_accion/libros.html')
    context = {}
    return HttpResponse(template.render(context, request))

def premezclas(request):
    template = loader.get_template('campos_accion/premezclas.html')
    context = {}
    return HttpResponse(template.render(context, request))

def revistas(request):
    template = loader.get_template('campos_accion/revistas.html')
    context = {}
    return HttpResponse(template.render(context, request))

def revista(request):
    template = loader.get_template('campos_accion/revista.html')
    context = {}
    return HttpResponse(template.render(context, request))
