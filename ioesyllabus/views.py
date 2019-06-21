from django.shortcuts import render, get_object_or_404
from .forms import SelectSyllabusForm
from .models import Subject

def homepage(request):
    if request.method == 'POST':
        form = SelectSyllabusForm(request.POST)
        if form.is_valid():
            faculty = form['faculty'].value()
            year = form['year'].value()
            part = form['part'].value()
            subjects = Subject.objects.filter(faculty=faculty, year=year, part=part)
            return render(request, 'index.html', {'subjects': subjects})
    else:
        form = SelectSyllabusForm()
    return render(request, 'index.html', {'form': form})

def view_syllabus(request, id):
    subject = get_object_or_404(Subject, pk=id)
    return render(request, 'show_syllabus.html', {'subject': subject})

def view_404(request, exception):
    return render(request, '404.html')
