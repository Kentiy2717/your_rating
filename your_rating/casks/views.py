from django.shortcuts import render
from django.views.generic import (
    TemplateView,
    DetailView
)


class IndexTemplateView(TemplateView):
    template_name = 'casks/index.html'


class ShowCaskView(DetailView):
    template_name = 'casks/cask.html'
