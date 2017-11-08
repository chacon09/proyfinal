from django.shortcuts import render,redirect,get_object_or_404
from django.contrib import messages
from .forms import DeportistaForm
from .forms import DeporteForm
from deportes.models import Deportista, Participacion, Deporte
from django.contrib.auth.decorators import login_required

def pelicula_nueva(request):
    if request.method == "POST":
        formulario = DeportistaForm(request.POST)
        if formulario.is_valid():
            deportista = Deportista.objects.create(nombre=formulario.cleaned_data['nombre'], edad = formulario.cleaned_data['edad'])
            for deporte_id in request.POST.getlist('deporte'):
                participacion = Participacion(deporte_id=deporte_id, deportista_id = deportista.id)
                participacion.save()
            messages.add_message(request, messages.SUCCESS, 'Participacion Guardada Exitosamente')
    else:
        formulario = DeportistaForm()
    return render(request, 'peliculas/pelicula_editar.html', {'formulario': formulario})
# Create your views here.

@login_required
def listar_deportista(request):
    pub = Deportista.objects.all()
    return render(request, 'peliculas/listar_pub.html', {'pub' : pub})

def editar_deportista(request,pk):
    deportista=get_object_or_404(Deportista,pk=pk)
    if request.method=="POST":
        form=DeportistaForm(request.POST,instance=deportista)

        if form.is_valid():
            deportista=form.save(commit=False)
            deportista.save()
            return redirect('listar_deportista')
        else:
            form=DeportistaForm(intance=deportista)
        return render(request,'peliculas/editar_deportista.html',{'form':form})

def borrar_deportista(request, pk):
    pub = get_object_or_404(Deportista, pk=pk)
    pub.delete()
    return redirect('listar_deportista')

def crear_deporte(request):
    if request.method == "POST":
        formu = DeporteForm(request.POST)
        if formu.is_valid():
            deporte= formu.save(commit=False)
            deporte.save()
            return redirect('deporte_listar')
    else:
        formu = DeporteForm()
    return render(request, 'peliculas/crear_deporte.html', {'formu' : formu})

def deporte_listar(request):
    pub = Deporte.objects.all()
    return render(request, 'peliculas/deporte_listar.html', {'pub' : pub})

def borrar_deporte(request, pk):
    pub = get_object_or_404(Deporte, pk=pk)
    pub.delete()
    return redirect('deporte_listar')

def editar_deporte(request,pk):
    deporte=get_object_or_404(Deporte,pk=pk)
    if request.method=="POST":
        form=DeporteForm(request.POST,instance=deporte)

        if form.is_valid():
            deporte=form.save(commit=False)
            deportista.save()
            return redirect('deporte_listar')
        else:
            form=DeportistaForm(intance=deportista)
        return render(request,'peliculas/deportee_editar.html',{'form':form})
