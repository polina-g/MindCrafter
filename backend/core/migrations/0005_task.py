# Generated by Django 5.1.3 on 2024-11-29 17:33

import core.models.fields.string
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_subtask'),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('description', models.TextField()),
                ('priority', core.models.fields.string.StringField(blank=True, choices=[('highest', 'Highest'), ('high', 'High'), ('low', 'Low'), ('lowest', 'Lowest')], null=True)),
                ('due_date_time', models.DateTimeField(blank=True, null=True)),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='core.taskcategory')),
                ('notes', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='core.tasknote')),
                ('status', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.taskstatus')),
                ('subtask', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='core.subtask')),
            ],
            options={
                'verbose_name': 'Task',
                'verbose_name_plural': 'Tasks',
                'db_table': 'task',
                'indexes': [models.Index(fields=['status'], name='task_status__c5d47c_idx'), models.Index(fields=['category'], name='task_categor_b6b07d_idx')],
            },
        ),
    ]
