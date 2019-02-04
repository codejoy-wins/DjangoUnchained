
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^other$', views.other),
    url(r'^addItem$', views.addItem),
    url(r'^dbAddItem$', views.dbAddItem),
    url(r'^display$', views.displayItems),
    url(r'^delete/(?P<item_id>\d+)$', views.destroy),

    url(r'^', views.odell),

]
