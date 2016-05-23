from django.conf.urls import include, url
from django.views.generic import TemplateView, RedirectView

from .views import WritingListView, WritingDetailView, MessageCreateView

urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name='index.html'), name='home'),
    url(r'^list/$', WritingListView.as_view(), name='list'),
    url(r'^list/(?P<pk>\d+)/$', WritingDetailView.as_view(), name='text'),
    url(r'^contact/$', MessageCreateView.as_view(), name='contact'),
    url(r'^thanks/$', TemplateView.as_view(template_name='thanks.html'), name='thanks'),
    url(r'^light/$', RedirectView.as_view(url='https://www.instagram.com/wizzarding/'), name='light'),

]
