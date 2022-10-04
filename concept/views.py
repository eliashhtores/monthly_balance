from rest_framework import viewsets
from .models import Concept
from .serializers import ConceptSerializer


class ConceptViewSet(viewsets.ModelViewSet):
    """API to manage concepts in the database"""

    queryset = Concept.objects.all().order_by('-type', 'name')
    serializer_class = ConceptSerializer

    def get_queryset(self):
        queryset = super().get_queryset()

        if (self.request.GET.get('type') is None):
            return queryset

        return queryset.filter(type=self.request.GET.get('type'))
