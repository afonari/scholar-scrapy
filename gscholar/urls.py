from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^api/get_orgs/', views.get_orgs, name='get_orgs'),
    url(r'^$', views.index, name='index'),
]
