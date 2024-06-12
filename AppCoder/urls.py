from django.urls import path
from AppCoder import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('about/', views.about, name='about'),
    path('crear_guitar/', views.crear_guitar, name='crear_guitar'),
    path('guitars/', views.guitars,name='guitars')
]
