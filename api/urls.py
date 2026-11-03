from django.urls import path
from api import views

urlpatterns = [
    path('About/', views.About.as_view()),
    path('Education/', views.Education.as_view()),
    path('Project/', views.Project.as_view())
]