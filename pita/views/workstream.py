from django.views import generic

from .. import models


class WorkstreamListView(generic.ListView):
    template_name = 'pita/workstream/list.html'
    context_object_name = 'workstream_list'

    def get_queryset(self):
        return models.Workstream.objects.order_by('target_date')
