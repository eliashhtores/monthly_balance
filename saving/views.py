from rest_framework import viewsets
from .models import Saving
from .serializers import SavingSerializer


class SavingViewSet(viewsets.ModelViewSet):
    """API to manage savings in the database"""

    queryset = Saving.objects.all()
    serializer_class = SavingSerializer

    def get_queryset(self):
        queryset = super().get_queryset()

        if (self.request.GET.get('start_date') is None):
            return queryset

        if (self.request.GET.get('end_date')):
            return queryset.filter(created__gte=self.request.GET.get('start_date'), created__lte=self.request.GET.get('end_date'))

        return queryset.filter(created__gte=self.request.GET.get('start_date'))
