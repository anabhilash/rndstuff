from models import *
from rest_framework import serializers

class CardDetailsserializer(serializers.HyperlinkedModelSerializer):
    class meta:
        model=CardDetails
        fields=('nickName','nameOnCard','expireDate','type','cardNumber')
