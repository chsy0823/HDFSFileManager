from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.getInstanceList, name='instance_list'),
    url(r'^instance_list$', views.getInstanceList, name='instance_list'),
    url(r'^instanceItem_list$', views.getInstanceItems, name='instanceItem_list'),
    url(r'^remove_list$', views.removeInstance, name='remove_list'),
]
