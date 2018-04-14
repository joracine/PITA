from django.db import models
from django.utils import timezone

from . import team


class Feature(models.Model):

    name = models.CharField(max_length=50,
                            help_text='Short recognizable name of the feature (50 char max).')
    description = models.CharField(max_length=1000,
                                   help_text='Description of the feature (1000 char max).')

    owner = models.ForeignKey(team.Team,
                              on_delete=models.SET_NULL,
                              blank=True,
                              null=True,
                              help_text='Team that primarily owns the feature.')

    # Maintenance fields
    created = models.DateTimeField(editable=False,
                                   default=None)
    last_updated = models.DateTimeField(editable=False,
                                        default=None)

    @staticmethod
    def get_icon():
        return 'pita/icons/ic_tab_black_24dp_2x.png'

    def __str__(self):
        return self.name + " (" + str(self.id) + ")"

    def save(self, *args, **kwargs):
        if not self.id:
            self.created = timezone.now()
        self.last_updated = timezone.now()
        return super(Feature, self).save(args, kwargs)

