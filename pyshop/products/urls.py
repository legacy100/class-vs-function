from django.urls import path
from . import views
from . views import CreateProduct, UpdateProduct, DeleteProduct

urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    path('product/add/', CreateProduct.as_view(), name='add'),
    path('product/<int:pk>/', UpdateProduct.as_view(), name='update'),
    path('product/<int:pk>/', DeleteProduct.as_view(),name='delete'),
    # path('<str:pk>/update/', views.UpdateProducts.as_view(), name='update-product'),
    # path('createproduct/', views.CreateProduct.as_view(), name='create-products'),
    # # path('create-product/', views.CreateProduct.as_view(), name='createproduct'),
]
