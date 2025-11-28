from django.urls import path
from inicio.views import inicio, otra, crear_camiseta, listar_camisetas, ver_camiseta, EditarCamisetas, EliminarCamisetas

urlpatterns = [
    path('',inicio,name="inicio"),
    path('otra/',otra,name="otra"),
    path('ver-camiseta/<int:id>/', ver_camiseta, name='ver'),
    path("editar-camiseta/<pk>/", EditarCamisetas.as_view(), name="editar"),
    path("eliminar-camiseta/<pk>/", EliminarCamisetas.as_view(), name="eliminar"),
    path('crear-camiseta/',crear_camiseta, name="crear"),
    path('listado-camisetas/', listar_camisetas, name="listado"),
]