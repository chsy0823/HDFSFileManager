from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.getList, name='getList'),
]
