from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import date, datetime
from ckeditor.fields import RichTextField

class Categoria(models.Model):
    nombre = models.CharField(max_length=255)
    
    def __str__(self):
        return self.nombre
    
    def get_absolute_url(self):
        return reverse('inicio')

class Perfil(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    biogra = models.TextField()
    avatar = models.ImageField(null=True, blank=True, upload_to="imagenes/perfil/")
    titulo = models.CharField(max_length=255, null=True, blank=True)
    urlfacebook = models.CharField(max_length=255, null=True, blank=True)
    urltwitter = models.CharField(max_length=255, null=True, blank=True)
    urlpersonal = models.CharField(max_length=255, null=True, blank=True)
    
    def __str__(self):
         return str(self.user) #Es para visualizar la información en el Admin
     
class Post(models.Model):
    titulo = models.CharField(max_length=255)
    titulo_tag = models.CharField(max_length=255, default="Mi_Blog")
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    cuerpo = RichTextField(null=True, blank=True)
    fecha_creacion = models.DateField(auto_now_add=True)
    categoria = models.CharField(max_length=255, default="sin_categoria")
    resumen = models.CharField(max_length=255, default="sin_categoria")
    megusta = models.ManyToManyField(User, related_name='posts')
    
    def totalmegusta(self):
        return self.megusta.count() #Conteo de los Me Gusta       

    def __str__(self):
        return self.titulo + '|' + str(self.autor) #Es para guardar la información
    
    def get_absolute_url(self):
        return reverse('detalle', args=(str(self.pk))) #Es para que tome la info del formulario y lo guarde y retorne a la página de detalles con la información del post
    

class Comentarios(models.Model):
    post = models.ForeignKey(Post, related_name="Comentarios", on_delete=models.CASCADE)
    nombre = models.CharField(max_length=255)
    comentario = models.TextField()
    fcomentario = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return '%s - %s' % (self.post.titulo, self.nombre)  


    