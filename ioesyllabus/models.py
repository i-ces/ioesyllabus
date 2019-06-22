from django.db import models

class Subject(models.Model):
    FACULTY_CHOICES = (
        ('BCT', 'BCT'),
        ('BEI', 'BEI'),
        ('BCE', 'BCE')
    )
    YEAR_CHOICES = (
        ('1', 'I'),
        ('2', 'II'),
        ('3', 'III'),
        ('4', 'IV')
    )
    PART_CHOICES = (
        ('1', 'I'),
        ('2', 'II')
    )

    subject_name = models.CharField(max_length=30, null=False)
    content = models.TextField(null=True)
    lecture_hours = models.IntegerField()
    practical_hours = models.IntegerField()
    total_marks = models.IntegerField()
    pass_marks = models.IntegerField()
    references = models.TextField()
    faculty = models.CharField(choices=FACULTY_CHOICES, max_length=4, null=False)
    year = models.CharField(choices=YEAR_CHOICES, max_length=2, null=False)
    part = models.CharField(choices=PART_CHOICES, max_length=2, null=False)

    def __str__(self):
        return self.subject_name