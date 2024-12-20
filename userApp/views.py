from django.shortcuts import render,redirect
from .forms import UsuarioForm

# Create your views here.
def new_usuario(request):
    form = UsuarioForm(request.POST, request.FILES)
    if request.method == "POST":
        #form = AlunoForms(request.POST, request.FILES)
        if form.is_valid():
            usuario = form.save()
            usuario.save()
            form = UsuarioForm()
    context={'form':form}
    return render(request, 'user/new_usuario.html', context)