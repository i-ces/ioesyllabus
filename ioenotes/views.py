from django.shortcuts import render, get_object_or_404
from .models import Note

def view_notes(request, id):
    subject_note = get_object_or_404(Note, pk=id)
    print(subject_note)
    return render(request, 'show_notes.html', {'note': subject_note})
