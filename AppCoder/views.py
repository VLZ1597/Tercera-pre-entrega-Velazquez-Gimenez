from django.shortcuts import render , redirect
from AppCoder.models import Guitar
from AppCoder.forms import CrearGuitarFormulario


def inicio(request):
    return render(request, 'AppCoder/index.html')

def about(request): 
    return render(request, 'about.html')

def guitar(request, marca, forma):
    guitar = Guitar(marca=marca, forma=forma)
    guitar.save()
    return render(request,'creacion.html', {"guitar": guitar})

def crear_guitar(request):

    formulario = CrearGuitarFormulario() 
    
    if request.method == 'POST':
        formulario = CrearGuitarFormulario(request.POST)
        if formulario.is_valid():
            datos = formulario.cleaned_data
            guitar=Guitar(marca=datos.get('marca'), forma=datos.get('forma'))
            guitar.save()
            return redirect('guitars')
            
    return render(request, 'AppCoder/crear_guitar.html', {'formulario': formulario})


def guitars(request):
    
    guitars = Guitar.objects.all()
    
    return render(request,'AppCoder/guitars.html', {'guitars': guitars})