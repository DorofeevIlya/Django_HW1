from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path("show_orders/<int:user_id>/", views.show_orders, name="show_orders"),
    path("orders_total/<int:user_id>/<str:interval>/", views.orders_total, name="orders_total"),
    path("add_goods/", views.add_goods, name="add_goods"),
    path("select_goods/", views.select_an_action, name="select_goods"),
    path("del_good/", views.del_good, name="del_good"),
    path('upload/', views.upload_image, name='upload_image'),
    path('uploadi/', views.add_images, name='upload_image')
    ]