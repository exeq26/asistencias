from apps.programa.models import AsignacionBeneficio, Programa, TipoAsistencia
from django.contrib import admin

# Register your models here.

admin.site.register(TipoAsistencia)
admin.site.register(Programa)
admin.site.register(AsignacionBeneficio)