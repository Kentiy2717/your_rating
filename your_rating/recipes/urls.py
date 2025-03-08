from django.urls import path

from . import views

app_name = 'recipes'

urlpatterns = [
    path('', views.IndexTemplateView.as_view(), name='index'),
]
