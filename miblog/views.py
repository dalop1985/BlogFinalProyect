from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Categoria, Comentarios
from .forms import PostFormulario, ActFormulario, ComentarioFormulario
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect

#def inicio(request):
 #   return render(request, 'inicio.html', {})

class vistaInicio(ListView):
    model = Post
    template_name = 'inicio.html'
    ordering = ['-fecha_creacion','-id']
    
    def get_context_data(self, *args, **kwargs):
        cate_menu = Categoria.objects.all()
        cont = super(vistaInicio, self).get_context_data(*args, **kwargs)
        cont["cate_menu"] = cate_menu
        return cont

def categoriaLista(request):
    cmlista = Categoria.objects.all()
    return render(request, 'categoriaLista.html', {'cmlista':cmlista})

def categoria(request, cate):
    postcategorias = Post.objects.filter(categoria=cate.replace('-', ' '))
    return render(request, 'categoria.html', {'cate':cate.title().replace('-', ' '), 'postcategorias':postcategorias})
    

class detallePost(DetailView):
    model = Post
    template_name = 'detallePost.html'
    
    def get_context_data(self, *args, **kwargs):
        cate_menu = Categoria.objects.all()
        cont = super(detallePost, self).get_context_data(*args, **kwargs)
        bute = get_object_or_404(Post, id=self.kwargs['pk'])
        totalmegusta = bute.totalmegusta()
        megust = False
        if bute.megusta.filter(id=self.request.user.id).exists():
            megust = True
        cont["cate_menu"] = cate_menu
        cont["totalmegusta"] = totalmegusta
        cont["megust"] = megust
        return cont

class nuevoPost(CreateView):
    model = Post
    form_class = PostFormulario #Llama a los campos del modelo para ser guardados
    template_name = 'nuevoPost.html'
    #fields = '__all__'
    #fields = ('titulo','cuerpo','titulo_tag')

class nuevaCategoria(CreateView):
    model = Categoria
    template_name = 'nuevaCategoria.html'
    fields = '__all__'


class actualizarPost(UpdateView):
    model = Post
    pk = Post.id
    form_class = ActFormulario
    template_name = 'actualizarPost.html'
    success_url = reverse_lazy('inicio')
    #fields = ('titulo','titulo_tag','cuerpo')

class borrarPost(DeleteView):
    model = Post
    template_name = 'borrarPost.html'
    success_url = reverse_lazy('inicio')

def vistaMegusta(request, pk):
    post = get_object_or_404(Post, id=request.POST.get('idpost'))
    liked = False
    if post.megusta.filter(id=request.user.id).exists():
        post.megusta.remove(request.user)
    else:
        post.megusta.add(request.user)
        liked = True
    return HttpResponseRedirect(reverse('detalle', args=[str(pk)]))

class nuevoComentario(CreateView):
    model = Comentarios
    form_class = ComentarioFormulario #Llama a los campos del modelo para ser guardados
    template_name = 'agregarComentario.html'
    #fields = '__all__'
    def form_valid(self, form):
        form.instance.post_id = self.kwargs['pk']
        return super().form_valid(form)
    success_url = reverse_lazy('inicio')

def acerca(request):
    return render(request, "acerca.html", {})