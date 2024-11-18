from rest_framework import viewsets
from .models import Evento, Participante
from .serializers import EventoSerializer, ParticipanteSerializer

# ViewSet para o modelo Evento
class EventoViewSet(viewsets.ModelViewSet):
    queryset = Evento.objects.all()
    serializer_class = EventoSerializer

# ViewSet para o modelo Participante
class ParticipanteViewSet(viewsets.ModelViewSet):
    queryset = Participante.objects.all()
    serializer_class = ParticipanteSerializer
