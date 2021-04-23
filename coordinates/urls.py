from django.urls import path
from . import views

urlpatterns = [
    path('coordinates/', views.MessageView.as_view()),
    path('<int:vemac_id>', views.MessageView.as_view()),
    path('', views.index),
]
