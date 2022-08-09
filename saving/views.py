from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import Saving, SavingDetail
from .serializers import SavingSerializer, SavingDetailSerializer


class SavingViewSet(viewsets.ModelViewSet):
    """API to manage Saving objects"""
    serializer_class = SavingSerializer
    queryset = Saving.objects.all().order_by('-id')

    def create(self, request, *args, **kwargs):
        saving = Saving.objects.create()
        saving.active = request.data['active']
        saving_details = request.data['saving_detail_set']

        details = [SavingDetail(
            saving=saving,
            number=saving_detail.get('number'),
            date=saving_detail.get('date'))
            for saving_detail in saving_details]

        try:
            saving.save()
            SavingDetail.objects.bulk_create(details)
            return Response(SavingSerializer(saving).data, status=status.HTTP_201_CREATED)
        except Exception as e:
            saving.delete()
            return Response({'message': str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def partial_update(self, request, *args, **kwargs):
        try:
            saving = Saving.objects.get(pk=kwargs['pk'])
            saving.active = not saving.active
            saving.save()
            return Response(SavingSerializer(saving).data, status=status.HTTP_200_OK)
        except Saving.DoesNotExist:
            message = 'Saving not found'
            return Response({'message': message}, status=status.HTTP_404_NOT_FOUND)


class SavingDetailViewSet(viewsets.ModelViewSet):
    """API to manage Saving details in the database"""

    queryset = SavingDetail.objects.all()
    serializer_class = SavingDetailSerializer

    def get_queryset(self):
        queryset = super().get_queryset()

        if (self.request.GET.get('saving') is not None):
            return queryset.filter(saving__id=self.request.GET.get('saving'))

        return queryset
