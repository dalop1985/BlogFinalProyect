from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy
from .forms import SignUpForm, EditProfileForm, PasswordChangingForm
from django.views.generic import DetailView
from miblog.models import Perfil

class VerPerfil(DetailView):
    model = Perfil
    template_name = 'registration/user_profile.html'
    
    def get_context_data(self, *args, **kwargs):
        usuarios = Perfil.objects.all()
        cont = super(VerPerfil, self).get_context_data(*args, **kwargs)
        perfilUsuario = get_object_or_404(Perfil, id=self.kwargs['pk'])
        cont["perfilUsuario"] = perfilUsuario
        return cont

class PasswordsChangeView(PasswordChangeView):
    form_class = PasswordChangingForm
    #form_class = PasswordChangeForm
    success_url = reverse_lazy('password_success')

def password_success(request):
    return render(request, 'registration/password_success.html', {})

class registroUsuario(generic.CreateView):
    form_class = SignUpForm
    template_name = 'registro/registro.html'
    success_url = reverse_lazy('inicio')

class editarUsuario(generic.UpdateView):
    form_class = EditProfileForm
    template_name = 'registration/edit_profile.html'
    success_url = reverse_lazy('inicio')
    
    def get_object(self):
        return self.request.user