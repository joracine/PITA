from colorful.fields import RGBColorField
from django.db import models
from django.utils import timezone


class Status(models.Model):
    class Meta:
        verbose_name_plural = "statuses"

    name = models.CharField(max_length=10,
                            unique=True,
                            blank=False,
                            null=False,
                            help_text='Name of status (10 char max).')

    description = models.CharField(max_length=1000,
                                   blank=False,
                                   null=False,
                                   help_text='Description of the status (1000 char max).')

    text_color = RGBColorField(blank=False,
                               null=False,
                               default=0x000000,
                               help_text='Text color for the status (RGB).')

    background_color = RGBColorField(unique=True,
                                     blank=False,
                                     null=False,
                                     default=0xFFFFFF,
                                     help_text='Background color for the status (RGB).')

    @staticmethod
    def get_icon():
        return 'pita/icons/ic_traffic_black_24dp_2x.png'

    # Maintenance fields
    created = models.DateTimeField(editable=False,
                                   default=None)

    last_updated = models.DateTimeField(editable=False,
                                        default=None)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.id:
            self.created = timezone.now()
        self.last_updated = timezone.now()
        return super(Status, self).save(args, kwargs)

