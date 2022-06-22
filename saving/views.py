from rest_framework import viewsets
from .models import Saving
from .serializers import SavingSerializer


class SavingViewSet(viewsets.ViewSet):
    """API to manage savings in the database"""

    queryset = Saving.objects.all()
    serializer_class = SavingSerializer
