from django.conf.urls import url

from .views import *

urlpatterns = [
    url(r'^$', IndexTemplate.as_view(), name='index'),
    url(r'^registrar$', RegistrarTemplate.as_view(),name='registrar'),
    url(r'^login/$', LoginTemplate.as_view(), name='login'),
    url(r'^logout/$', LogoutView.as_view(), name='logout'),
    url(r'^search$', SearchView.as_view(), name='search'),
    url(r'^edit/(?P<pk>\d+)/$', EditView.as_view(), name='editar'),
    url(r'^eliminar/(?P<pk>\d+)/$', DeleteView.as_view(),name='eliminar'),
    url(r'^views/(?P<pk>[\w\-]+)/$', EmpleadoView.as_view(),name='vista'),
    url(r'^validar/$', ValidarHuella.as_view(), name='validar'),
    url(r'^empleados/$', EmpleadoPage.as_view(), name='lista'),
]
