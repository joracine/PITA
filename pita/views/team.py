from django.views import generic

from .. import models


class TeamListView(generic.ListView):
    template_name = 'pita/team/list.html'
    context_object_name = 'team_list'

    def get_queryset(self):
        return models.Feature.objects.order_by('name')
