"""mustang URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, include
from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
#    url(r'^list/$', views.ListView.as_view(), name='list'),
    #url(r'^action_list/$', views.index, name='index'),
]

# адреса для форм добавления.редактирования.удаления car
from .other_views import car_views
urlpatterns += [
    url(r'^cars/$', car_views.CarListView.as_view(), name='cars'),
    path(r'^car/(?P<pk>)/$', car_views.CarDetailView.as_view(), name='car-detail'),
    path(r'^car/create/$', car_views.CarCreate.as_view(), name='car_create'),
    path(r'^car/(?P<pk>)/update/$', car_views.CarUpdate.as_view(), name='car_update'),
    path(r'^car/(?P<pk>)/delete/$', car_views.CarDelete.as_view(), name='car_delete'),
]

# адреса для форм добавления.редактирования.удаления instrument
from .other_views import instrument_views
urlpatterns += [
    url(r'^instruments/$', instrument_views.InstrumentListView.as_view(), name='instruments'),
    path(r'^instrument/(?P<pk>)/$', instrument_views.InstrumentDetailView.as_view(), name='instrument-detail'),
    path(r'^instrument/create/$', instrument_views.InstrumentCreate.as_view(), name='instrument_create'),
    path(r'^instrument/(?P<pk>)/update/$', instrument_views.InstrumentUpdate.as_view(), name='instrument_update'),
    path(r'^instrument/(?P<pk>)/delete/$', instrument_views.InstrumentDelete.as_view(), name='instrument_delete'),
]

# адреса для форм добавления.редактирования.удаления service
from .other_views import service_views
urlpatterns += [
    url(r'^services/$', service_views.ServiceListView.as_view(), name='services'),
    path(r'^service/(?P<pk>)/$', service_views.ServiceDetailView.as_view(), name='service-detail'),
    path(r'^service/create/$', service_views.ServiceCreate.as_view(), name='service_create'),
    path(r'^service/(?P<pk>)/update/$', service_views.ServiceUpdate.as_view(), name='service_update'),
    path(r'^service/(?P<pk>)/delete/$', service_views.ServiceDelete.as_view(), name='service_delete'),
]
