from django.views import generic

from .. import models


class MilestoneListView(generic.ListView):
    template_name = 'pita/milestone/list.html'
    context_object_name = 'milestone_list'

    def get_queryset(self):
        return models.Milestone.objects.order_by('acronym')

