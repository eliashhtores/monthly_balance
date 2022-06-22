from rest_framework import viewsets
from .models import Investment
from .serializers import InvestmentSerializer


class InvestmentViewSet(viewsets.ModelViewSet):
    """API to manage investments in the database"""

    queryset = Investment.objects.all()
    serializer_class = InvestmentSerializer

    def get_queryset(self):
        queryset = super().get_queryset()

        if (self.request.GET.get('start_date') is None):
            return queryset

        if (self.request.GET.get('end_date')):
            return queryset.filter(start_date__gte=self.request.GET.get('start_date'), start_date__lte=self.request.GET.get('end_date'))

        return queryset.filter(start_date__gte=self.request.GET.get('start_date'))
