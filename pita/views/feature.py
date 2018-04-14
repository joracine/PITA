from django.views import generic

from .. import models


class FeatureListView(generic.ListView):
    template_name = 'pita/feature/list.html'
    context_object_name = 'feature_list'

    def get_queryset(self):
        return models.Feature.objects.order_by('name')
