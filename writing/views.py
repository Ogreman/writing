from django.core.mail import send_mail, mail_admins
from django.shortcuts import render
from django.core.urlresolvers import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView
from django.conf import settings
from django.core import serializers
from django.http import JsonResponse

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


class WritingDetailAPIView(ActiveObjectMixin, DetailView):
    model = Writing

    def get(self, request, *args, **kwargs):
        obj = self.get_object()
        data = serializers.serialize("json", [obj], fields=('title', 'content'))
        return JsonResponse(data, status=200, safe=False)


class WritingListAPIView(ActiveObjectMixin, ListView):
    model = Writing

    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        data = serializers.serialize("json", queryset, fields=('title', 'content'))
        return JsonResponse(data, status=200, safe=False)


class MessageCreateView(CreateView):
    model = Message
    form_class = MessageForm
    template_name = "contact.html"
    success_url = reverse_lazy('thanks')

    def form_valid(self, form):
        response = super(MessageCreateView, self).form_valid(form)
        site_url = settings.SITE_URL
        url = reverse('admin:writing_message_change', args=(self.object.id, ))
        mail_admins('New message on Wizzarding', 'Check the admin page for details',
            html_message=settings.NEW_MESSAGE_TEMPLATE.format(site_url, url), fail_silently=True)
        return response