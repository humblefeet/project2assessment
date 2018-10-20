from django.urls import path, include
from . import views

urlpatterns =  [
    path('', views.base, name='base'),
    path('add/', views.AddWidget, name="widget_form"),
    path('<int:pk>/delete/', views.WidgetDelete.as_view(), name="widget_delete"),
]