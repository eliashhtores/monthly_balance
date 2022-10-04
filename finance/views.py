from datetime import date, datetime
from django.db.models import Q
from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import Finance
from .serializers import FinanceSerializer


class FinanceViewSet(viewsets.ModelViewSet):
    """API to manage Finance objects"""
    serializer_class = FinanceSerializer
    queryset = Finance.objects.all().order_by('due_date')

    def get_queryset(self):
        queryset = super().get_queryset()

        if self.request.GET.get('type') is None:
            return queryset

        queryset = queryset.filter(concept__type=self.request.GET.get('type'))

        start_date = self.request.GET.get('start_date')
        end_date = self.request.GET.get('end_date')

        if (start_date is None):
            current_month = datetime.now().month
            current_year = datetime.now().year
            return queryset.filter(Q(due_date__year__gte=current_year) & Q(due_date__month__range=(current_month, current_month)))

        if (end_date):
            return queryset.filter(due_date__range=(start_date, end_date))

        return queryset.filter(due_date__gte=start_date)

    def partial_update(self, request, *args, **kwargs):
        try:
            finance = Finance.objects.get(pk=kwargs['pk'])
            if finance.paid == False:
                finance.paid = True
                finance.pay_date = date.today()
            else:
                finance.paid = False
                finance.pay_date = None
            finance.save()
            return Response(FinanceSerializer(finance).data, status=status.HTTP_200_OK)
        except Finance.DoesNotExist:
            message = 'Finance not found'
            return Response({'message': message}, status=status.HTTP_404_NOT_FOUND)
