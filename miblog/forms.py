from django import forms
from .models import Post, Categoria, Comentarios

#Opción para el listado de las Categorías
opciones = Categoria.objects.all().values_list('nombre','nombre')
lista_opciones = []
for i in opciones:
    lista_opciones.append(i)

class PostFormulario(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('titulo','titulo_tag','autor','categoria','cuerpo','resumen')
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Introduce el Título'}),
            'titulo_tag': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Introduce el Tag'}),
            'autor': forms.Select(attrs={'class': 'form-control'}),
            'categoria': forms.Select(choices=lista_opciones, attrs={'class': 'form-control'}), 
            'cuerpo': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Acá va el texto del post'}),
            'resumen': forms.Textarea(attrs={'class': 'form-control'}),
                                           
        }
#Para la creación del formulario y así poder definir sus estilos con el css que usa bootstrap

class ActFormulario(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('titulo','titulo_tag','categoria','cuerpo','resumen')
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Introduce el Título'}),
            'titulo_tag': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Introduce el Tag'}),
            'categoria': forms.Select(choices=lista_opciones, attrs={'class': 'form-control'}),
            'cuerpo': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Acá va el texto del post'}),
            'resumen': forms.Textarea(attrs={'class': 'form-control'}),                       
        }

class ComentarioFormulario(forms.ModelForm):
    class Meta:
        model = Comentarios
        fields = ('nombre','comentario')
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Introduce el Nombre'}),
            'comentario': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Agrega el comentario'}),
        }