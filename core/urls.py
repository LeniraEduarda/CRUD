
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
]


urlpatterns = [
    path('create/', views.create_alvo, name='create_alvo'),
    path('list/', views.list_alvos, name='list_alvos'),
    path('update/<int:pk>/', views.update_alvo, name='update_alvo'),
    path('delete/<int:pk>/', views.delete_alvo, name='delete_alvo'),
]