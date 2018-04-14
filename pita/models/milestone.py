from colorful.fields import RGBColorField
from django.db import models
from django.utils import timezone


class Milestone(models.Model):

    acronym = models.CharField(max_length=5,
                               help_text='Unique acronym by which milestone is often referred by (5 char max).',
                               unique=True,
                               db_index=True)

    name = models.CharField(max_length=50,
                            help_text='Short name for the milestone (50 char max).')

    description = models.CharField(max_length=1000,
                                   help_text='Description of the milestone (1000 char max).')

    text_color = RGBColorField(blank=False,
                               null=False,
                               default=0,
                               help_text='Text color for the milestone (RGB).')

    background_color = RGBColorField(unique=True,
                                     blank=False,
                                     null=False,
                                     default=0xFFFFFF,
                                     help_text='Background color for the milestone (RGB).')

    @staticmethod
    def get_icon():
        return 'pita/icons/ic_today_black_24dp_2x.png'

    # Maintenance fields
    created = models.DateTimeField(editable=False,
                                   default=None)

    last_updated = models.DateTimeField(editable=False,
                                        default=None)

    def __str__(self):
        return '[' + self.acronym + "] " + self.name + " (" + str(self.id) + ")"

    def save(self, *args, **kwargs):
        if not self.id:
            self.created = timezone.now()
        self.last_updated = timezone.now()
        return super(Milestone, self).save(args, kwargs)