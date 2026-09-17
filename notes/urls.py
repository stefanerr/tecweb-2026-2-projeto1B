from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('editar/<int:note_id>', views.edit, name='edit'),
    path('deletar/<int:note_id>', views.delete, name='delete'),
]