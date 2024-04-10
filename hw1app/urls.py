from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path("show_orders/<int:user_id>/", views.show_orders, name="show_orders"),
    path("orders_total/<int:user_id>/<str:interval>/", views.orders_total, name="orders_total"),
    ]