from django.conf.urls import include, url
from django.views.generic import TemplateView

from .views import WritingListView, WritingDetailView

urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name='index.html')),
    url(r'^list/$', WritingListView.as_view(), name='list'),
    url(r'^list/(?P<pk>\d+)/$', WritingDetailView.as_view(), name='text'),
]
