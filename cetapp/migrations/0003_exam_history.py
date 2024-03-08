# Generated by Django 4.2.1 on 2023-06-11 12:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cetapp', '0002_exam_alter_userdata_id_exam_data'),
    ]

    operations = [
        migrations.CreateModel(
            name='Exam_history',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ans_list', models.TextField(null=True)),
                ('exam_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cetapp.exam')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cetapp.userdata')),
            ],
        ),
    ]