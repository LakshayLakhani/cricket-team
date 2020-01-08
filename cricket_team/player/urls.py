from django.conf.urls import url

from player.views import AddPlayer, PlayerListView, PlayerDetailView


urlpatterns = [
    url(r'^add/$', AddPlayer, name='add_player'),
    url(r'^$', PlayerListView.as_view(), name='player_list'),
    url(r'^(?P<slug>[\w-]+)/$', PlayerDetailView.as_view(), name='player_detail'),
]
