from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic

from .. import models


class PriorityListView(generic.ListView):
    template_name = 'pita/priority/list.html'
    context_object_name = 'priority_list'

    def get_queryset(self):
        return models.Priority.objects.order_by('weight')


class ResetPrioritiesConfirmationView(generic.TemplateView):
    template_name = 'pita/priority/reset_confirmation.html'


def process_reset_priorities(request):
    confirmation = request.POST['confirm']
    if confirmation == "yes":
        models.Priority.objects.all().delete()

        models.Priority(name='P0',
                        long_name='Ship Blocker',
                        description='Vital feature, deliverable, or workstream, that would block launch if it was cut.',
                        weight=100).save()

        models.Priority(name='P1',
                        long_name='Critical',
                        description='Critical feature, deliverable, or workstream that would not block launch if it was cut.',
                        weight=200).save()

        models.Priority(name='P2',
                        long_name='Nice-to-Have',
                        description="Important feature, deliverable, or workstream that should be pursued to delight customers, but isn't critical to the product.",
                        weight=300).save()

        models.Priority(name='P3',
                        long_name='Aspirational',
                        description='Feature, deliverable, or workstream that should not be planned to be worked on, but signal where the product should go next.',
                        weight=400).save()

    return HttpResponseRedirect(reverse('list_priorities'))

class ResetPrioritiesSuccessView(generic.TemplateView):
    template_name = 'pita/status/reset_success.html'
