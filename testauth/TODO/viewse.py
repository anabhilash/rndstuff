from models import *
from rest_framework import viewsets
from seria import ListSerializers

class ListViewSet(viewsets.ModelViewSet):
    queryset=TodoList.objects.all()
    serializer_class=ListSerializers

