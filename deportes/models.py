from django.db import models

from django.contrib import admin

class Deporte(models.Model):
    nombre  =   models.CharField(max_length=30)
    descripcion = models.CharField(max_length=60)

    def __str__(self):
        return self.nombre

class Deportista(models.Model):
    nombre    = models.CharField(max_length=60)
    edad     = models.IntegerField()
    deportes   = models.ManyToManyField(Deporte, through='Participacion')

    def __str__(self):
        return self.nombre

class Participacion (models.Model):
    
    deporte = models.ForeignKey(Deporte, on_delete=models.CASCADE)
    deportista = models.ForeignKey(Deportista, on_delete=models.CASCADE)

class ParticipacionInLine(admin.TabularInline):
    model = Participacion
    extra = 1


class DeporteAdmin(admin.ModelAdmin):
    inlines = (ParticipacionInLine,)


class DeportistaAdmin (admin.ModelAdmin):
    inlines = (ParticipacionInLine,)
