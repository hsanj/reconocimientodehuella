from django.conf.urls import include, url
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import FormularioQueja,quejaCreateView

urlpatterns = [
    
    
    #path('formulario_queja/',quejaCreateView.as_view(),name='formulario_queja'),
    path('formulario_queja/',FormularioQueja.as_view(),name='formulario_queja'),

]