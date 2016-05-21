from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import Writing, View


class ActiveObjectMixin(object):

    def get_queryset(self):
        queryset = super(ActiveObjectMixin, self).get_queryset()
        queryset = queryset.filter(active=True)
        return queryset


class WritingListView(ActiveObjectMixin, ListView):
    model = Writing
    template_name = "list.html"


class WritingDetailView(ActiveObjectMixin, DetailView):
    model = Writing
    template_name = "text.html"

    def get_object(self, queryset=None):
        obj = super(WritingDetailView, self).get_object(queryset)
        if not self.request.user.is_authenticated():
            View.objects.create(writing=obj)
        return obj