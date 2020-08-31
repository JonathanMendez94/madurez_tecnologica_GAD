from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin
# Register your models here.


class CategoriasAdmin(admin.ModelAdmin):
    search_fields = ['categoria']
admin.site.register(Categorias,CategoriasAdmin)

class EncuestasAdmin(admin.ModelAdmin):
    search_fields = ['nombre']
admin.site.register(Encuestas,EncuestasAdmin)

class FichasAdmin(admin.ModelAdmin):
    search_fields = ['fecha','usuario']
    list_display = ('fecha','gad_servi_usuario','pregunta_respuesta')
    #fields = ('respuesta','fecha','usuario')
admin.site.register(Fichas,FichasAdmin)

class GadAdmin(admin.ModelAdmin):
    search_fields = ['gad']
admin.site.register(Gad,GadAdmin)

class GadServiciosAdmin(admin.ModelAdmin):
    search_fields = ['gad', 'servicios','fecha']
    list_display = ('gad', 'servicios','fecha')
admin.site.register(GadsServicios,GadServiciosAdmin)

class PreguntasAdmin(admin.ModelAdmin):
    search_fields = ['pregunta','encuesta','categoria']
    #fields = ('pregunta','encuesta','subcategoria')
    list_display = ('pregunta','encuesta','categoria')
admin.site.register(Preguntas, PreguntasAdmin)

class PreguntasRespuestasAdmin(admin.ModelAdmin):
    search_fields = ['pregunta','respuesta','valor']
    list_display = ('pregunta','respuesta','valor')
    list_filter = ['pregunta']
    raw_id_fields = ('pregunta','respuesta')
admin.site.register(PreguntasRespuestas, PreguntasRespuestasAdmin)

class RespuestasAdmin(admin.ModelAdmin):
    search_fields = ['respuesta']
admin.site.register(Respuestas,RespuestasAdmin)

class ServiciosAdmin(admin.ModelAdmin):
    search_fields = ['servicio']
admin.site.register(Servicios,ServiciosAdmin)



