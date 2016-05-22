from django.shortcuts import render
from django.core.urlresolvers import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView

from .models import Writing, View, Message
from .forms import MessageForm


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


class MessageCreateView(CreateView):
    model = Message
    form_class = MessageForm
    template_name = "contact.html"
    success_url = reverse_lazy('thanks')