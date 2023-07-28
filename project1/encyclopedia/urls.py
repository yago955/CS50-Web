from django.urls import path
from . import views



urlpatterns = [
    path('random/', views.random_page, name='random'),
    path('edit/<str:title>/', views.edit, name='edit'),
    path('save_edit/<str:title>/', views.save_edit, name='save_edit'),
    path('new_page/', views.new_page, name='new_page'),
    path('search/', views.search, name='search'),
    path("wiki/<str:title>", views.entry, name="entry"),
    path("", views.index, name="index")
]
