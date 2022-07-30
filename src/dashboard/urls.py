from django.urls import path
from .views import *
from .recipe import views as rec_view
from .category import views as ctg_view

urlpatterns = [
    path('', home, name='dashboard_home'),
    path('rec/list/', rec_view.list_detail_delete, name='dashboard_rec_list'),
    path('rec/detail/<int:pk>/', rec_view.list_detail_delete, name='dashboard_rec_detail'),
    path('rec/delete/<int:delete>/', rec_view.list_detail_delete, name='dashboard_rec_delete'),
    path('rec/add/', rec_view.add_edit, name='dashboard_rec_add'),
    path('rec/edit/<int:pk>/', rec_view.add_edit, name='dashboard_rec_edit'),

#    path('', home, name='dashboard_home'),
    path('ctg/list/', ctg_view.list_detail_delete, name='dashboard_ctg_list'),
    path('ctg/detail/<int:pk>/', ctg_view.list_detail_delete, name='dashboard_ctg_detail'),
    path('ctg/delete/<int:delete>/', ctg_view.list_detail_delete, name='dashboard_ctg_delete'),
    path('ctg/add/', ctg_view.add_edit, name='dashboard_ctg_add'),
    path('ctg/edit/<int:pk>/', ctg_view.add_edit, name='dashboard_ctg_edit'),
]
