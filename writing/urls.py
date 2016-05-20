from django.conf.urls import include, url
from django.views.generic import TemplateView

from .views import WritingListView

urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name='index.html')),
    url(r'^list/$', WritingListView.as_view(), name='list'),
]
