from django.conf.urls import url
from django.urls import path
from .views import ProductosView,ProductoDetalleView

urlpatterns = [
    path('',ProductosView.as_view(),name='index'),
    path('<slug:slug>',ProductoDetalleView.as_view(),name='producto_detalle'),
]