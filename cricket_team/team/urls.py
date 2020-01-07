from django.conf.urls import url

from team.views import TeamListView

urlpatterns = [
    url(r'^$', TeamListView.as_view(), name='team_list'),
]
