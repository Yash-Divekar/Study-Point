# Generated by Django 4.2.1 on 2023-06-12 04:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cetapp', '0007_alter_exam_history_user_ans'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exam',
            name='exam_status',
            field=models.TextField(max_length=50),
        ),
    ]
