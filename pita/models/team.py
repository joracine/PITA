from django.core.exceptions import ValidationError
from django.db import models
from django.utils import timezone


class Team(models.Model):

    name = models.CharField(max_length=20,
                            unique=True,
                            db_index=True,
                            help_text='Short name of the team, often but not always an acronym (20 char max).')

    descriptive_name = models.CharField(max_length=1000,
                                        help_text='Long descriptive name of the team (1000 char max).')

    description = models.CharField(max_length=5000,
                                   blank=True,
                                   null=True,
                                   help_text='Description of the team (5000 char max).')

    parent = models.ForeignKey('self',
                               on_delete=models.SET_NULL,
                               blank=True,
                               null=True,
                               help_text='Parent team or organization. Cannot be self.')

    # Maintenance fields
    created = models.DateTimeField(editable=False,
                                   default=None)
    last_updated = models.DateTimeField(editable=False,
                                        default=None)


    @staticmethod
    def get_icon():
        return 'pita/icons/ic_people_black_24dp_2x.png'

    def __str__(self):
        return self.name + " (" + self.descriptive_name + ')'

    def save(self, *args, **kwargs):
        if self.parent == self.id and self.parent is not None:
            raise ValidationError('Parent (' + str(self.parent) + ') cannot point to itself (' + str(self.id) + ').')

        if not self.id:
            self.created = timezone.now()
        self.last_updated = timezone.now()
        return super(Team, self).save(args, kwargs)

