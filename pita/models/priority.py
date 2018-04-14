from django.db import models
from django.utils import timezone

class Priority(models.Model):
    class Meta:
        verbose_name_plural = "priorities"

    name = models.CharField(max_length=2,
                            help_text='Short name that represents priority (2 char max).',
                            unique=True,
                            null=False,
                            blank=False,
                            db_index=True)

    long_name = models.CharField(max_length=50,
                                 null=False,
                                 blank=False,
                                 help_text='Long name of the priority (50 char max).')

    description = models.CharField(max_length=1000,
                                   help_text='Description of the priority (1000 char max).',
                                   null=True,
                                   default=None)

    weight = models.PositiveIntegerField(unique=True,
                                         null=False,
                                         blank=False,
                                         help_text='Weight when comparing priorities. A lower weight means item is more important (0 is highest). Must be unique.')

    @staticmethod
    def get_icon():
        return 'pita/icons/ic_change_history_black_24dp_2x.png'

    # Maintenance fields
    created = models.DateTimeField(editable=False,
                                   default=None)
    last_updated = models.DateTimeField(editable=False,
                                        default=None)

    def __str__(self):
        return '[' + self.name + "] " + self.long_name + " (" + str(self.id) + ")"

    def save(self, *args, **kwargs):
        if not self.id:
            self.created = timezone.now()
        self.last_updated = timezone.now()
        return super(Priority, self).save(args, kwargs)

