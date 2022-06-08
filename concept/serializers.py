from rest_framework import serializers
from .models import Concept


class ConceptSerializer(serializers.ModelSerializer):
    """Serializer for concept objects"""

    type = serializers.CharField(source='get_type_display')

    class Meta:
        model = Concept
        fields = '__all__'
