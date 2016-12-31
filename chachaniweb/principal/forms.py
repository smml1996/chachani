from django import forms

class ContactoForm(forms.Form):
    nombre = forms.CharField(label = "nombre" ,max_length = 50)
    apellidos = forms.CharField(label ="apellidos" ,max_length = 50)
    number = forms.IntegerField(label = "number", required = False)
    email = forms.EmailField()
    departamento = forms.CharField(label = "departamento" ,max_length = 30)
    provincia = forms.CharField(label = "provincia" ,max_length = 30)
    mensaje = forms.CharField(widget=forms.Textarea,label = "mensaje" )
