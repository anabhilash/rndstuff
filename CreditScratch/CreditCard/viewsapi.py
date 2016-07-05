from models import *
from rest_framework import viewsets
from serializers import *
class CardDetailsviewset(viewsets.ModelViewSet):
    queryset=CardDetails.objects.all()
    serializer_class = CardDetailsserializer