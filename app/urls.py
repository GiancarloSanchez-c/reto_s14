from django.urls import path
from django.contrib.auth.decorators import login_required
from app.views import AutoCreate, AutoUpdate, AutoDelete, AutoList, Products, DetailList, MenuAuto


urlpatterns = [
    path('autos/create', login_required(AutoCreate.as_view()), name='autos_create'),
    path('menu',login_required(MenuAuto.as_view()), name='menu'),
    path('autos/listProducts', login_required(AutoList.as_view()), name='autos_list'),
    path('autos/update/<pk>', login_required(AutoUpdate.as_view()), name='autos_update'),
    path('autos/delete/<pk>', login_required(AutoDelete.as_view()), name='autos_delete'),
    path('autos/products', login_required(Products.as_view()),name='autos_products'),
    path('detail/list/<pk>', login_required(DetailList.as_view()), name='detail_list'),
]