from rest_framework import serializers
from concept.models import Concept
from .models import Finance


class FinanceSerializer(serializers.ModelSerializer):
    """Serializer for finance objects"""
    concept = serializers.SlugRelatedField(
        slug_field='id', queryset=Concept.objects.all())

    def to_representation(self, instance):
        rep = super(FinanceSerializer, self).to_representation(instance)
        rep['concept'] = instance.concept.name
        rep['concept_id'] = instance.concept.id
        return rep

    class Meta:
        model = Finance
        fields = '__all__'
        read_only_fields = ('id',)
