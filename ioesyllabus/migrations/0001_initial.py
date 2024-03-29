# Generated by Django 2.2.2 on 2019-06-18 13:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject_name', models.CharField(max_length=30)),
                ('content', models.TextField()),
                ('lecture_hours', models.IntegerField()),
                ('practical_hours', models.IntegerField()),
                ('total_marks', models.IntegerField()),
                ('pass_marks', models.IntegerField()),
                ('references', models.TextField()),
            ],
        ),
    ]
