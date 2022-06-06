from django.db import models
from model_utils.models import TimeStampedModel


class Investment(TimeStampedModel):
    initial_amount = models.IntegerField()
    percentage = models.DecimalField(max_digits=4, decimal_places=2)
    start_date = models.DateField()
    end_date = models.DateField()
    completed = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.initial_amount} - {self.percentage}%'
