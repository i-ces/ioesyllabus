from django.urls import path
from .views import view_notes

urlpatterns = [
    path('<int:id>/', view_notes, name='view_notes')
]