from django.urls import path
from contact import views

app_name = 'contact'
 
urlpatterns = [
    path('<int:contact_id>/', views.contact, name='contact'),  # Corrigido 'int' para 'path'
    path('search/', views.search, name='search'),  # Corrigido 'int' para 'path'
    path('', views.index, name='index'),
]