from django.urls import path

from .import views

urlpatterns = [
	path('save',views.save, name='save'),
	path('read',views.read, name='read'),
	path('write',views.write, name='write'),
    path('', views.home, name='home')
]

