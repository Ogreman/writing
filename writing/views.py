from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import Writing


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
