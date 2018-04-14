from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic

from .. import models


class StatusListView(generic.ListView):
    template_name = 'pita/status/list.html'
    context_object_name = 'status_list'

    def get_queryset(self):
        return models.Status.objects.order_by('name')


class ResetStatusesConfirmationView(generic.TemplateView):
    template_name = 'pita/status/reset_confirmation.html'


def process_reset_statuses(request):
    confirmation = request.POST['confirm']
    if confirmation == "yes":
        models.Status.objects.all().delete()

        models.Status(name='Green',
                      description='Feature, deliverable, or workstreams on track.',
                      text_color=0x000000,
                      background_color=0x006400).save()

        models.Status(name='Yellow',
                      description='Feature, deliverable, or workstreams has significant risk, and might not be on track, but has a path to green.',
                      text_color=0x000000,
                      background_color=0xFFA500).save()

        models.Status(name='Red',
                      description='Feature, deliverable, or workstreams is not on track, with no path to green.',
                      text_color=0x000000,
                      background_color=0x8B0000).save()

        models.Status(name='Deferred',
                      description='Feature, deliverable, or workstreams has been deferred to a later milestone or release.',
                      text_color=0x000000,
                      background_color=0xFFA07A).save()

        models.Status(name='Need Date',
                      description='Feature, deliverable, or workstreams doe not have a target date yet and status is unknown.',
                      text_color=0x000000,
                      background_color=0x1E90FF).save()

    return HttpResponseRedirect(reverse('reset_statuses_success'))


class ResetStatusesSuccessView(generic.TemplateView):
    template_name = 'pita/status/reset_success.html'

