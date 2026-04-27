
from django.urls import path
from . import views

urlpatterns = [
    path('', views.session_list, name= 'session_list'),
    path('add/', views.add_session, name='add_session'),
    path('delete/<int:id>/', views.delete_session, name= 'delete_session'),
    path('update/<int:id>/', views.update_session, name= 'update_session'),
    path('signup/', views.sign_up,name='sign_up'),
]