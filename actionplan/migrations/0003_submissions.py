# Generated by Django 3.2.7 on 2021-10-19 03:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('actionplan', '0002_auto_20210929_1637'),
    ]

    operations = [
        migrations.CreateModel(
            name='Submissions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stage1_file', models.FileField(upload_to='submissions/stage1')),
                ('stage2_file', models.FileField(upload_to='submissions/stage2')),
                ('stage3_file', models.FileField(upload_to='submissions/stage3')),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
