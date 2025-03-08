from django.urls import path

from . import views

app_name = 'drinks'

urlpatterns = [
    path('', views.IndexTemplateView.as_view(), name='index'),
]
