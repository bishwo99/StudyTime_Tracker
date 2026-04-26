
from django.urls import path
from . import views

urlpatterns = [
    path('', views.session_list, name= 'session_list'),
    path('add/', views.add_session, name='add_session'),
    path('delete/<int:id>/', views.delete_session, name= 'delete_session'),
]