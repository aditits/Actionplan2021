# Generated by Django 3.2.7 on 2021-09-29 11:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('actionplan', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='name_of_organisation',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='team',
            name='referral_code',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='team',
            name='team_member3_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='team',
            name='team_member4_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='team',
            name='team_member5_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='team',
            name='team_member6_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='team',
            name='team_member7_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='team',
            name='team_member8_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
