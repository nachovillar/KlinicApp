from django.urls import path

from . import views

urlpatterns = [
    path('', views.lista_pacientes, name='lista'),
    path('nuevo/', views.nuevo_paciente, name='nuevo'),
    path('crear/', views.crear_paciente, name='crear'),
    path("saludo/", views.index, name='saludo'),
    path('<str:rut>/', views.info_paciente, name='info_paciente') ,
    path('<str:rut>/ficha/nueva', views.nueva_ficha, name='nueva_ficha'),
    path('<str:rut>/ficha/crear', views.crear_ficha, name='crear_ficha'),
    path('<str:rut>/ficha/<int:id>', views.ficha, name='ficha')
]

