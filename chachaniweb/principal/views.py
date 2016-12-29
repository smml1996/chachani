from django.http import HttpResponse, Http404
from django.template import loader
from django.db import connection
import json

def index(request):
    template = loader.get_template('index.html')
    context = {}
    return HttpResponse(template.render(context, request))

def nosotros(request):
    template = loader.get_template('nosotros.html')
    context = {}
    return HttpResponse(template.render(context, request))

def contacto(request):
    template = loader.get_template('contacto.html')
    return HttpResponse(template.render({},request))

def error(request):
    template = loader.get_template('404error.html');
    return HttpResponse(template.render({},request))
def InsertContacto(request):
    nombre = request.POST.get("nombre","")
    response_data={}
    try:
        nombre = request.POST.get("nombre","")
        apellido = request.POST.get("apellido","")
        dep = request.POST.get("dep","")
        prov = request.POST.get("prov","")
        mail = request.POST.get("mail","")
        num = request.POST.get("num","")
        mensaje = request.POST.get("mensaje","")
        response_data={}
        sql = 'INSERT INTO tcontacto( nombre, apellido, departamento, provincia, mail, numero, mensaje) VALUES ("'+nombre+'","'+apellido+'","'+dep+'","'+prov+'","'+mail+'","'+num+'","'+mensaje+'")'
        curs = connection.cursor()
        curs.execute(sql)
        response_data['result']="Exito"
        response_data['message']=nombre
    except:
        response_data['result']="Error"
        response_data['message']="Error"
    return HttpResponse(json.dumps(response_data),content_type="application/json")
