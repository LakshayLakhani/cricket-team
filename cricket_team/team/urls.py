from django.conf.urls import url

from team.views import TeamListView, TeamDetailView


urlpatterns = [
    url(r'^$', TeamListView.as_view(), name='team_list'),
    url(r'^(?P<slug>[\w-]+)/$', TeamDetailView.as_view(), name='team_detail'),
]
