# Generated by Django 2.2.3 on 2019-08-07 04:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0005_auto_20190805_1144'),
    ]

    operations = [
        migrations.AddField(
            model_name='userdetails',
            name='question_attended',
            field=models.ManyToManyField(to='quiz.Question'),
        ),
    ]
