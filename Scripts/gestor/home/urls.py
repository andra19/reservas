from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='index'),
    path('info/', views.info, name='informacion'),
    path('final/', views.final, name='final')
    # path('', views.Login, name='ingreso')
]