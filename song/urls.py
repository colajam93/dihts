from django.conf.urls import url
from song import views

urlpatterns = [
    url(r'^$', views.search, name='search'),
]
