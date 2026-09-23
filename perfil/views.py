from django.shortcuts import render

# Create your views here.
def perfil_uno(request):
    data = {"nombre": "El condor pasa", "año": "1995", "correo": "condor@gmail.com"}
    return render(request, 'perfil/p1.html',data)

def perfil_dos(request):
    data = {"nombre": "Matikanefukukitaru", "año": "1994", "correo": "fukukitaru@gmail.com"}
    return render(request, 'perfil/p2.html',data)