from django.urls import path
from .views import registroUsuario, editarUsuario, PasswordsChangeView, VerPerfil
from django.contrib.auth import views as auth_views
from .import views 

urlpatterns = [
    path('registro/', registroUsuario.as_view(), name='Registro'),
    path('editarPerfil/', editarUsuario.as_view(), name='Editar'),
    #path('password/', auth_views.PasswordChangeView.as_view(template_name='registration/cambiarContraseña.html')), **Vista a la página del admin para el cambio de contraseña**
    path('password/', PasswordsChangeView.as_view(template_name='registration/cambiarContrasena.html')),
    path('password_success', views.password_success, name="password_success"),
    path('vistaPerfil/<int:pk>', VerPerfil.as_view(), name='vistaPerfil'),
    
]
 