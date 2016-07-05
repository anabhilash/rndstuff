from rest_framework import serializers
from models import *
class ListSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=TodoList
        fields=('name','created')


class ItemSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
            model=TodoItem
            fields=('description','created','duedate','completed','li')