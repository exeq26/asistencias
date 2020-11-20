from django.urls import path
from .views import asignar_beneficio, detalle_befenicio, programa_lista, programa_detalle, programa_create, programa_edit, programa_delete


app_name = 'programa'
urlpatterns = [
    # programa views
    path('', programa_lista, name='programa_lista'),
    path('<int:pk>/', programa_detalle, name='programa_detalle'),
    path('create/', programa_create, name='programa_create'),
    path('edit/<int:pk>', programa_edit, name='programa_edit'),
    path('delete/', programa_delete, name='programa_delete'),
    path('asignar/',asignar_beneficio,name='asignar_beneficio'),
    path('<int:pk>/',detalle_befenicio, name='detalle_beneficio'),
]
