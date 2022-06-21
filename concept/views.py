from rest_framework import viewsets
from .models import Concept
from .serializers import ConceptSerializer


class ConceptViewSet(viewsets.ModelViewSet):
    """API to manage concepts in the database"""

    queryset = Concept.objects.order_by('-type', 'name')
    serializer_class = ConceptSerializer
