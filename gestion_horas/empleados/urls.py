from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_view, name='login'),  # Login ahora es la raíz
    path('panel_control/', views.panel_control, name='panel_control'),  # Nueva URL para el panel de control
    path('registrar/', views.registrar_entrada, name='registrar'),  # Página de registro
    path('registrar_salida/', views.registrar_entrada, name='registrar_salida'), 
    path('tabla_registros/', views.ver_registros, name='tabla_registros'),  # Tabla de registros
    path('solicitudes/', views.solicitudes, name='solicitudes'),  # Nueva vista de solicitudes
    path('enviar_solicitud/', views.enviar_solicitud, name='enviar_solicitud'),  # Nueva vista para enviar solicitud
    path('panel_control/', views.panel_control, name='panel_control'),  # URL para la vista
    path('solicitudes_pendientes/', views.solicitudes_pendientes, name='solicitudes_pendientes'),  # URL para solicitudes pendientes
    path('exportar/', views.exportar_datos, name='exportar'),  # URL para exportar

]
