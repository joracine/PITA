from django.db import models
from django.utils import timezone

from . import status
from . import team


class Workstream(models.Model):

    team = models.ForeignKey(team.Team,
                             on_delete=models.SET_NULL,
                             blank=True,
                             null=True,
                             help_text='Team that owns the delivery of the workstream.')

    name = models.CharField(max_length=50,
                            blank=False,
                            null=False,
                            help_text='Long name of the priority (50 char max).')

    description = models.CharField(max_length=1000,
                                   help_text='Description of the priority (100 char max).',
                                   null=True,
                                   default=None)

    target_date = models.DateField(blank=True,
                                   null=True,
                                   help_text='Date at which the workstream should be completed.')

    status = models.ForeignKey(status.Status,
                               on_delete=models.SET_NULL,
                               blank=True,
                               null=True,
                               help_text='Latest status of the workstream.')

    # Maintenance fields
    created = models.DateTimeField(editable=False,
                                   default=None)

    last_updated = models.DateTimeField(editable=False,
                                        default=None)

    @staticmethod
    def get_icon():
        return 'pita/icons/ic_tab_unselected_black_24dp_2x.png'

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.id:
            self.created = timezone.now()
        self.last_updated = timezone.now()
        return super(Workstream, self).save(args, kwargs)

