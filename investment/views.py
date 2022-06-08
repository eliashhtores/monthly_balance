from rest_framework import viewsets
from .models import Investment
from .serializers import InvestmentSerializer


class InvestmentViewSet(viewsets.ModelViewSet):
    """API to manage investments in the database"""

    queryset = Investment.objects.all()
    serializer_class = InvestmentSerializer
