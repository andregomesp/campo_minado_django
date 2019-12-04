from django.urls import path

from . import views

app_name = 'canpo_minado_app'
urlpatterns = [
    path('', views.index, name='index')
]
