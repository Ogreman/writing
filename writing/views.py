from django.shortcuts import render
from django.views.generic import ListView

from .models import Writing


class WritingListView(ListView):
    model = Writing
    template_name = "list.html"