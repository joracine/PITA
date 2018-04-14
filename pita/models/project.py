from django.db import models
from django.utils import timezone

from . import team


class Project(models.Model):

    name = models.CharField(max_length=20,
                            unique=True,
                            blank=False,
                            null=False,
                            help_text='Name of the project (20 char max).')

    codename = models.CharField(max_length=20,
                                unique=20,
                                blank=False,
                                null=False,
                                help_text='Code name for the project (20 char max).')

    description = models.CharField(max_length=2000,
                                   blank=True,
                                   null=True,
                                   help_text='Description of the project (2000 char max).')

    owner = models.ForeignKey(team.Team,
                              on_delete=models.SET_NULL,
                              blank=True,
                              null=True,
                              help_text='Team that owns the project.')

    # Maintenance fields
    created = models.DateTimeField(editable=False,
                                   default=None)

    last_updated = models.DateTimeField(editable=False,
                                        default=None)

    @staticmethod
    def get_icon():
        return 'pita/icons/ic_aspect_ratio_black_24dp_2x.png'

    def __str__(self):
        return self.codename + " (" + self.codename + ")"

    def save(self, *args, **kwargs):
        if not self.id:
            self.created = timezone.now()
        self.last_updated = timezone.now()
        return super(Project, self).save(args, kwargs)

