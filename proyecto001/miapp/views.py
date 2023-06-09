from django.http import HttpResponse
from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
layout = """
    <h1>Proyecto Web (LP3) | David Rosado</h1>
    <hr/>
    <ul>
        <li>
            <a href="/inicio">Inicio</a>
        </li>
        <li>
            <a href="/saludo">Mensaje de saludo</a>
        </li>
        <li>
            <a href="/rango">Mostrar números</a>
        </li>
        <li>
            <a href="/rango2/10/15"> Mostrar Números [10,15]</a>
        </li>
    </ul>
    <hr/>
"""


def index(request):
    estudiantes = ['Isabella Caballero',
                   'Alejandro Hermitaño',
                   'Joan Palomino',
                   'Pierre Bernaola']

    return render(request, 'index.html', {
        'titulo': 'Inicio',
        'mensaje': 'Proyecto Web con Django',
        'estudiantes':estudiantes
    })


def saludo(request):
    return render(request, 'saludo.html', {
        'titulo': 'Saludo',
        'autor_saludo': 'David Rosado Valerio'
    })


def rango(request):
    a = 10
    b = 20
    rango_numeros = range(a, b + 1)
    return render(request, 'rango.html', {
        'titulo':'Rango',
        'a':a,
        'b':b,
        'rango_numero':rango_numeros
    })


def rango2(request, a=0, b=100):
    if a > b:
        return redirect('rango2', a=b, b=a)
    resultado = f"""
        <h2>Numeros de [{a}, {b}]</h2>
        Resultado: <br>
        <ul>
    """
    while a <= b:
        resultado += f"<li> {a} </li>"
        a += 1
    resultado += "</ul"
    return HttpResponse(layout + resultado)
