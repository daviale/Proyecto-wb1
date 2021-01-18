from django.urls import path
from .views import RolListView, DireccionListView, CategoryListView, UsuarioListView, ProductListView, ListsListView, ClientListView

urlpatterns = [
    path('rol/', RolListView.as_view(), name='rol_list'),
    path('direccion/', DireccionListView.as_view(), name='direccion_list'),
    path('category/', CategoryListView.as_view(), name='category_list'),
    path('usuario/', UsuarioListView.as_view(), name='usuario_list'),
    path('product/', ProductListView.as_view(), name='product_list'),
    path('lists/', ListsListView.as_view(), name='lists_list'),
    path('client/', ClientListView.as_view(), name='client_list')
]