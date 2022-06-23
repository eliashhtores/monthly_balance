from rest_framework import serializers
from .models import Saving, SavingDetail


class SavingDetailSerializer(serializers.ModelSerializer):
    """Serializer for saving detail objects"""

    class Meta:
        model = SavingDetail
        fields = '__all__'
        read_only_fields = ('id',)


class SavingSerializer(serializers.ModelSerializer):
    """Serializer for saving detail objects"""

    saving_detail_set = SavingDetailSerializer(many=True)

    class Meta:
        model = Saving
        fields = '__all__'
        read_only_fields = ('id',)
