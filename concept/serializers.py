from rest_framework import serializers
from .models import Concept


class ChoiceField(serializers.ChoiceField):
    def to_representation(self, obj):
        if obj == '' and self.allow_blank:
            return obj
        return self._choices[obj]

    def to_internal_value(self, data):
        if data == '' and self.allow_blank:
            return ''

        for key, val in self._choices.items():
            if val == data:
                return key
        self.fail('invalid_choice', input=data)


class ConceptSerializer(serializers.ModelSerializer):
    """Serializer for concept objects"""

    type = ChoiceField(choices=Concept.CONCEPT_CHOICES)

    class Meta:
        model = Concept
        fields = '__all__'
        read_only_fields = ('id',)
