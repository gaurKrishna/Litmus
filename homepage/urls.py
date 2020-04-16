from django.conf.urls import url
from . import views

app_name = 'homepagedemo'

urlpatterns = [
    # /homepagedemo/
    url(r'^$', views.index, name = 'index'),
    # /homepagedemo/addnotes/
    url(r'^addnotes/$', views.add, name = 'add'),
]