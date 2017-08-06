from django.conf.urls import url
from . import views

urlpatterns = [
     url(r'^$', views.notes, name='notes'),
     url(r'^calendar/$', views.calendar, name='calendar'),
     url(r'^add/$', views.add, name='add'),
     url(r'^about/$', views.about, name='about'),
]
