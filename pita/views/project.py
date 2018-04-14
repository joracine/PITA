from django.views import generic

from .. import models


class ProjectListView(generic.ListView):
    template_name = 'pita/project/list.html'
    context_object_name = 'feature_list'

    def get_queryset(self):
        return models.Project.objects.order_by('codename')
