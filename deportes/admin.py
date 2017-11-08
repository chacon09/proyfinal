from django.contrib import admin
from deportes.models import Deporte, DeporteAdmin, Deportista, DeportistaAdmin

admin.site.register(Deporte, DeporteAdmin)
admin.site.register(Deportista, DeportistaAdmin)
