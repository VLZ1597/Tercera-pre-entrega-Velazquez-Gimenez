from django.shortcuts import render , redirect
from AppCoder.models import Guitar
from AppCoder.forms import CrearGuitarFormulario , BuscarGuitar


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
    
    formulario = BuscarGuitar(request.GET)
    if formulario.is_valid():   
        marca = formulario.cleaned_data['marca']        
        guitar = Guitar.objects.filter(marca__icontains=marca)

    return render(request,'AppCoder/guitars.html', {'guitars': guitar ,'formulario': formulario})

def eliminar_guitar(request,id):
    guitar = Guitar.objects.get(id=id)
    guitar.delete()
    return redirect('guitars')  


def ver_guitar(request,id):
    guitar = Guitar.objects.get(id=id)
    return render(request, 'AppCoder/ver_guitar.html', {'guitar': guitar})