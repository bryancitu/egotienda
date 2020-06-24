from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView
from .models import *

class ProductosView(TemplateView):
    template_name = "productos/index.html"
    
    def get_context_data(self, **kwargs):
        kwargs['productos'] = Producto.objects.all()
        return kwargs

class ProductoDetalleView(TemplateView):
    template_name = "productos/producto_detalle.html"
    
    def get_context_data(self, **kwargs):
        libro_slug = kwargs.get('slug')
        kwargs['producto'] = Producto.objects.get(slug=libro_slug)
        return kwargs