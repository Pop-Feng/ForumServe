# Generated by Django 3.1.7 on 2021-04-01 12:37

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ForumServe', '0008_questions'),
    ]

    operations = [
        migrations.CreateModel(
            name='QandA',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_id', models.CharField(blank=True, max_length=100)),
                ('answer_name', models.CharField(blank=True, max_length=100)),
                ('answer_content', models.CharField(blank=True, max_length=100)),
                ('answer_date', models.DateTimeField(default=datetime.datetime.now)),
            ],
        ),
    ]
