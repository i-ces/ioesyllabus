from django.db import models

class subject(models.model)
FACULTY_CHOICES =(
    ('BCT','BCT'),
    ('BEI','BEI'),
    ('BCE','BCE')
)
YEAR_CHOICES =(
    ('1','I'),
    ('2','II'),
    ('3','III'),
    ('4','IV')
)
PART_CHOICES =(
    ('1','I'),
    ('2','II')
)
subject_name = models.Charfield(max_length=30,null=False)
preface = models.TextField(null=False)
content = models.TextField(null=False)
chapters =models.Charfield(max_length=20,null=False)
faculty = models.Charafield(choices=FaACULTY_CHOICES,max_length=4,null=False)
year = models.CharField(choices=YEAR_CHOICES,max_length=2,null=False)
part=models.CharField(choices=PART_CHOICES,max_length=2,null=False)

def __str__(self):
        return self.subject_name