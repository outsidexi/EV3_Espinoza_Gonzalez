from django.contrib.auth.models import User
from django.db import models
from django.utils.timezone import now

class RegistroHoras(models.Model):
    empleado = models.ForeignKey(User, on_delete=models.CASCADE)
    fecha = models.DateField(default=now)
    hora_entrada = models.TimeField(null=True, blank=True)
    hora_salida = models.TimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.empleado.username} - {self.fecha}"


