from django.urls import path

from . import views

app_name = 'casks'

urlpatterns = [
    path('', views.IndexTemplateView.as_view(), name='index'),
    path('<slug:cask_slug>/', views.ShowCaskView.as_view(), name='cask_page'),
]