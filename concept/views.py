from rest_framework import viewsets
from .models import Concept
from .serializers import ConceptSerializer


class ConceptViewSet(viewsets.ModelViewSet):
    queryset = Concept.objects.all()
    serializer_class = ConceptSerializer
