
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^other$', views.other),
    url(r'^', views.odell),

]
