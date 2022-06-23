from rest_framework import viewsets
from .models import Saving, SavingDetail
from .serializers import SavingSerializer, SavingDetailSerializer


class SavingViewSet(viewsets.ModelViewSet):
    """API to manage Saving objects"""
    serializer_class = SavingSerializer
    queryset = Saving.objects.all().order_by('-id')


class SavingDetailViewSet(viewsets.ModelViewSet):
    """API to manage Saving details in the database"""

    queryset = SavingDetail.objects.all()
    serializer_class = SavingDetailSerializer

    def get_queryset(self):
        queryset = super().get_queryset()

        if (self.request.GET.get('saving') is not None):
            return queryset.filter(saving__id=self.request.GET.get('saving'))

        return queryset
