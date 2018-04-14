from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.index, name='index'),

    path('project/list/', views.ProjectListView.as_view(), name='list_projects'),

    path('priority/list/', views.PriorityListView.as_view(), name='list_priorities'),
    path('priority/reset/', views.process_reset_priorities, name='reset_priorities'),
    path('priority/reset_confirm/', views.ResetPrioritiesConfirmationView.as_view(),
         name='reset_priorities_confirmation'),
    path('priority/reset_success/', views.process_reset_priorities, name='reset_priorities_success'),

    path('feature/list/', views.FeatureListView.as_view(), name='list_features'),

    path('milestone/list/', views.MilestoneListView.as_view(), name='list_milestones'),

    path('workstream/list/', views.WorkstreamListView.as_view(), name='list_workstreams'),

    path('teams/list/', views.TeamListView.as_view(), name='list_teams'),

    path('statuses/list/', views.StatusListView.as_view(), name='list_statuses'),
    path('statuses/reset/', views.process_reset_statuses, name='reset_statuses'),
    path('statuses/reset_confirm/', views.ResetStatusesConfirmationView.as_view(),
         name='reset_statuses_confirmation'),
    path('statuses/reset_success/', views.ResetStatusesSuccessView.as_view(), name='reset_statuses_success'),

    # Admin
    path('grappelli/', include('grappelli.urls')),
    path('admin/', admin.site.urls),
]
