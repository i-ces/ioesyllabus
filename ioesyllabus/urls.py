from django.urls import path
from .views import view_syllabus

urlpatterns = [
    path('<int:id>/', view_syllabus, name='view_syllabus')
]