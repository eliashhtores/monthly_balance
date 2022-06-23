from rest_framework import serializers
from .models import Saving, SavingDetail


class SavingSerializer(serializers.ModelSerializer):
    """Serializer for saving detail objects"""

    class Meta:
        model = Saving
        fields = '__all__'
        read_only_fields = ('id',)


class SavingDetailSerializer(serializers.ModelSerializer):
    """Serializer for saving detail objects"""

    class Meta:
        model = SavingDetail
        fields = '__all__'
        read_only_fields = ('id',)
