from django.urls import path
from myapp_01 import views

app_name = 'myapp_01'

urlpatterns = [
    #path(r'list/', views.ContatoList.as_view(), name='list'),
    path(r'<int:pk>/', views.ADetailView.as_view(), name='detail'),
    path(r'add/', views.ACreateView.as_view(), name='create'),
    path(r'update/<int:pk>/', views.AUpdateView.as_view(), name='update'),
]
