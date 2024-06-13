from django.urls import path
from AppCoder import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('about/', views.about, name='about'),
    path('crear_guitar/', views.crear_guitar, name='crear_guitar'),
    path('guitars/', views.guitars,name='guitars'),
    path('eliminar/<int:id>', views.eliminar_guitar,name='eliminar_guitar'),
    path('ver/<int:id>', views.ver_guitar,name='ver_guitar'),
]
    