from django.urls import path
from . import views


urlpatterns = [
    path('addTask/', views.addTask, name='addTask'),
    path('mark_as_done/<int:pk>/', views.mark_as_done, name="mark_as_done"),
    path('delet_task/<int:pk>/', views.delet_task, name="delet_task"),
    #mark as undone
    path('mark_as_undone/<int:pk>/', views.mark_as_undone, name="mark_as_undone"),

    #Edit Fetaure 
    path('edit_task/<int:pk>/', views.edit_task, name='edit_task'),
]