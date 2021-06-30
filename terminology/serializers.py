from terminology.models import Element,Directory
from rest_framework import serializers


class ElementSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Element
        fields = ['parent', 'code', 'value',]



class DirectorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Directory
        fields = ['name', 'short_name', 'description', 'version', 'date']
