from rest_framework import serializers
from .models import Investment


class InvestmentSerializer(serializers.ModelSerializer):
    """Serializer for investment objects"""

    class Meta:
        model = Investment
        fields = '__all__'
        read_only_fields = ('id',)
