from django.db import models
from model_utils.models import TimeStampedModel


class Saving(TimeStampedModel):
    active = models.BooleanField(default=True)

    def __str__(self):
        return str(self.id)


class SavingDetail(TimeStampedModel):
    saving = models.ForeignKey(
        Saving, on_delete=models.CASCADE, related_name='saving_detail_set'
    )
    number = models.IntegerField(default=1)
    date = models.DateField()
    paid = models.BooleanField(default=False)
    payback = models.IntegerField(blank=True, null=True)

    class Meta:
        unique_together = ('number', 'date')
        ordering = ('number', 'date')

    def __str__(self):
        return f'{str(self.number)} - {str(self.date)}'
