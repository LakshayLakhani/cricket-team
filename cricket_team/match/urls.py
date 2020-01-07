from django.conf.urls import url

from match.views import add_match

urlpatterns = [
    url(r'^add/$', add_match, name='add_match'),
]
