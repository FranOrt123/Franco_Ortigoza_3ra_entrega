from django.urls import path
from inicio.views import inicio, otra, crear_camiseta, listar_camisetas

urlpatterns = [
    path('',inicio),
    path('otra/',otra),
    path('crear-camiseta/<club>/<modelo>/<talle>',crear_camiseta),
    path('listado-camisetas/', listar_camisetas),
]