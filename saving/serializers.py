from rest_framework import serializers
from .models import Saving


class SavingSerializer(serializers.ModelSerializer):
    """Serializer for saving objects"""

    class Meta:
        model = Saving
        fields = '__all__'
        read_only_fields = ('id',)
