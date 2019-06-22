from django.db import models
from ioesyllabus.models import Subject

class Note(models.Model):
    subject = models.OneToOneField(Subject, on_delete=models.CASCADE)
    content = models.TextField(null=False)

    def __str__(self):
        return self.subject.subject_name