from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import Writing


class WritingListView(ListView):
    model = Writing
    template_name = "list.html"


class WritingDetailView(DetailView):
    model = Writing
    template_name = "text.html"