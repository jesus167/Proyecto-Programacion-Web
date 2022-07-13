from django import forms

class formulario_contacto(forms.Form):

    nombre = forms.CharField(label='Nombre', max_length=50, required=True)

    email = forms.EmailField(label='Email', required=True)

    contenido = forms.CharField(label='Contenido', widget=forms.Textarea)
