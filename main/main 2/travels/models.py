from django.db import models
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.forms import ModelForm

# Create your models here.
class TravelPlan(models.Model):
    destination = models.CharField(
        max_length=255,
    )
    travel_start_date = models.DateField()
    travel_end_date = models.DateField()
    plan = models.CharField(
        max_length=255,
    )

    owner = models.ForeignKey(User)
    # print 'OOOKKK'

    def __str__(self):
        return ', '.join([
            self.destination,
            # str(self.travel_start_date),
            # str(self.travel_end_date),
            # self.plan,
        ])

    def get_absolute_url(self):
        return reverse('travelplan-view', kwargs={'pk': self.id})

class TravelPlanForm(ModelForm):
    class Meta:
        model = TravelPlan
        fields = ['destination', 'travel_start_date', 'travel_end_date', 'plan']
