from django.urls import path
from .views import (
    CategoryListCreateView, 
    ProductListCreateView, 
    CategoryDetail, 
    ProductDetail,
    CartCreateView,
    CartProductCreateView
    )


urlpatterns = [
    path('categories/', CategoryListCreateView.as_view()),
    path('categories/<int:pk>/', CategoryDetail.as_view()),
    path('products/', ProductListCreateView.as_view()),
    path('products/<int:pk>/', ProductDetail.as_view()),
    path('cart/', CartCreateView.as_view()),
    path('cartproduct/', CartProductCreateView.as_view()),

]
