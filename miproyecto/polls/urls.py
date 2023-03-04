from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('hola/', views.holamanuel, name='hola'),
    path('<int:id_pregunta>/', views.detalle, name='detalle'),
    path('<int:id_pregunta>/resultados/', views.resultados, name='resultados'),
    path('<int:id_pregunta>/votando/', views.votar, name='votar')
]
