from django.contrib import admin
from .models import Evento, Participante

@admin.register(Evento)
class EventoAdmin(admin.ModelAdmin):
    list_display = ('id_eventos', 'nome', 'data', 'local')
    search_fields = ['nome']
    list_filter = ['data', 'local']

    def has_change_permission(self, request, obj=None):
        if not request.user.is_superuser:
            return False
        return super().has_change_permission(request, obj)

    def has_delete_permission(self, request, obj=None):
        if not request.user.is_superuser:
            return False
        return super().has_delete_permission(request, obj)

@admin.register(Participante)
class ParticipanteAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'email', 'Evento')
    search_fields = ['nome', 'email']
    list_filter = ['Evento']