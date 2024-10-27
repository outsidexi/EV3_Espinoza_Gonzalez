from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import RegistroHoras
from django.utils.timezone import now
from django.utils.dateparse import parse_datetime
from django.http import HttpResponse


from django.contrib.auth.decorators import login_required

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Redirige según el tipo de usuario
            if user.is_superuser:  # Verifica si el usuario es un superusuario
                return redirect('registrar')  
            else:
                return redirect('panel_control')  
        else:
            messages.error(request, 'Usuario o contraseña incorrectos')
    return render(request, 'empleados/login.html')


@login_required
def registrar_entrada(request):
    if request.method == 'POST':
        fecha_hora_entrada = request.POST.get('entrada_fecha_hora')
        entrada = parse_datetime(fecha_hora_entrada)  # Convierte el string a un objeto datetime

        RegistroHoras.objects.create(empleado=request.user, fecha=entrada.date(), hora_entrada=entrada.time())
        return redirect('registrar')

    return render(request, 'empleados/registrar.html')

@login_required
def registrar_salida(request):
    if request.method == 'POST':
        fecha_hora_salida = request.POST.get('salida_fecha_hora')
        salida = parse_datetime(fecha_hora_salida)  # Convierte el string a un objeto datetime

        registro = RegistroHoras.objects.filter(empleado=request.user, fecha=salida.date()).first()
        if registro and not registro.hora_salida:
            registro.hora_salida = salida.time()
            registro.save()

        return redirect('registrar')

    return render(request, 'empleados/registrar.html')

@login_required
def ver_registros(request):
    registros = RegistroHoras.objects.filter(empleado=request.user).order_by('-fecha')
    return render(request, 'empleados/tabla_registros.html', {'registros': registros})

@login_required
# Vista para mostrar la página de solicitudes
def solicitudes(request):
    return render(request, 'empleados/solicitudes.html')

# Vista para procesar la solicitud de tiempo libre
def enviar_solicitud(request):
    if request.method == 'POST':
        rut = request.POST.get('rut')
        fecha_inicio = request.POST.get('fecha_inicio')
        fecha_fin = request.POST.get('fecha_fin')
        motivo = request.POST.get('motivo')
        
        # Aquí puedes agregar la lógica para guardar la solicitud en la base de datos
        # Por ejemplo: Solicitud.objects.create(rut=rut, fecha_inicio=fecha_inicio, fecha_fin=fecha_fin, motivo=motivo)

        # Redirigir a una página de éxito o mostrar un mensaje
        return HttpResponse("Solicitud enviada con éxito.")

    return redirect('solicitudes')



def panel_control(request):
    # Datos de ejemplo
    trabajadores = [
        {'nombre': 'Paulina Donoso', 'hora_entrada': '13:00', 'hora_salida': '19:00'},
        {'nombre': 'Rexy Kotcho', 'hora_entrada': '13:01', 'hora_salida': '19:00'},
        {'nombre': 'Magna Tello', 'hora_entrada': '12:00', 'hora_salida': '19:00'},
    ]
    return render(request, 'empleados/panel_control.html', {'trabajadores': trabajadores})



def solicitudes_pendientes(request):
    # Datos de ejemplo
    solicitudes_pendientes = [
        {
            'empleado': 'Paulina Donoso',
            'motivo': 'Vacaciones',
            'fecha_inicio': '2024-07-15',
            'fecha_fin': '2024-07-20'
        },
        {
            'empleado': 'Rexy Kotcho',
            'motivo': 'Asunto Personal',
            'fecha_inicio': '2024-08-01',
            'fecha_fin': '2024-08-03'
        },
        {
            'empleado': 'Magna Tello',
            'motivo': 'Exámenes',
            'fecha_inicio': '2024-08-10',
            'fecha_fin': '2024-08-15'
        },
    ]
    return render(request, 'empleados/solicitudes_pendientes.html', {'solicitudes': solicitudes})

def exportar_datos(request):
    return render(request, 'empleados/exportar.html')