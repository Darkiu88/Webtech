from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('custom-case/', views.custom_case, name='custom_case'),
    path('cus/', views.cus_view, name='cus_view'),
    path('pre-build', views.pre_build, name='pre_build'),
    path('pre-build-gaming/', views.pre_build_gaming, name='pre_build_gaming'),
    path('pre-build-escuela/', views.pre_build_escuela, name='pre_build_escuela'),
    path('pre-build-trabajo/', views.pre_build_trabajo, name='pre_build_trabajo'),
]