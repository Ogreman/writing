from django.conf.urls import include, url
from django.views.generic import TemplateView, RedirectView

from .views import (
    WritingListView, WritingDetailView, MessageCreateView,
    WritingDetailAPIView, WritingListAPIView)

urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name='index.html'), name='home'),
    url(r'^list/$', WritingListView.as_view(), name='list'),
    url(r'^list/(?P<pk>\d+)/$', WritingDetailView.as_view(), name='text'),
    url(r'^contact/$', MessageCreateView.as_view(), name='contact'),
    url(r'^thanks/$', TemplateView.as_view(template_name='thanks.html'), name='thanks'),
    url(r'^vikings/$', TemplateView.as_view(template_name='vikings.html'), name='vikings'),
    url(r'^light/$', RedirectView.as_view(url='https://www.instagram.com/wizzarding/'), name='light'),
    url(r'^twitter/$', RedirectView.as_view(url='https://www.twitter.com/a_WIZZARD/'), name='twitter'),

    url(r'^api/list/$', WritingListAPIView.as_view(), name='api_list'),
    url(r'^api/list/(?P<pk>\d+)/$', WritingDetailAPIView.as_view(), name='api_detail'),
]
