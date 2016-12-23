from django.http import HttpResponse, Http404
from django.template import loader

def alimento(request):
    template = loader.get_template('campos_accion/alimento.html')
    context = {}
    return HttpResponse(template.render(context, request))

def carne(request):
    template = loader.get_template('campos_accion/carne.html')
    context = {}
    return HttpResponse(template.render(context, request))

def cultivo(request):
    template = loader.get_template('campos_accion/cultivo.html')
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

def lotes(request):
    template = loader.get_template('campos_accion/lotes.html')
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

def tilapias(request):
    template = loader.get_template('campos_accion/tilapias.html')
    context = {}
    return HttpResponse(template.render(context, request))
