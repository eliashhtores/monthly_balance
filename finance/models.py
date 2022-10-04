from django.db import models
from model_utils.models import TimeStampedModel
from concept.models import Concept


class Finance(TimeStampedModel):
    PAYMENT = 'PAY'
    LOAN = 'LOAN'
    TYPE_CHOICES = (
        (PAYMENT, 'Payment'),
        (LOAN, 'Loan'),
    )
    FIRST = 'First'
    SECOND = 'Second'
    TIME_FRAME_CHOICES = (
        (FIRST, 1),
        (SECOND, 2),
    )

    name = models.CharField(max_length=100, null=True, blank=True)
    amount = models.FloatField()
    concept = models.ForeignKey(
        Concept, on_delete=models.CASCADE
    )
    type = models.CharField(
        max_length=4, choices=TYPE_CHOICES, default=LOAN
    )
    time_frame = models.CharField(
        max_length=6, choices=TIME_FRAME_CHOICES, null=True, blank=True)
    date = models.DateField()
    due_date = models.DateField(null=True, blank=True)
    paid = models.BooleanField(default=False, null=True, blank=True)
    pay_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return f'{self.name} - {str(self.amount)}'
