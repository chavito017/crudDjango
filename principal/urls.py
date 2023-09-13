from django.urls import path
from .import views
from principal.views import *

urlpatterns = [
path('', views.home, name='home'),
    path('registrarUsuario/', views.registrarUsuario),
    path('edicionUsuario/<codigo>', views.edicionUsuario),
    path('editarUsuario/<int:usuario_id>/', views.editarUsuario, name='editar_usuario'),
    path('eliminarUsuario/<int:id>/', views.eliminarUsuario, name='eliminar_usuario'),
    path('temas/', views.HomeT, name='tema'),

]

