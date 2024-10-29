# Generated by Django 5.1.1 on 2024-10-23 03:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0015_customuser_profile_pic_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='contact_no',
            field=models.CharField(choices=[('recruiter', 'Recruiter'), ('seeker', 'Seeker')], max_length=100, null=True),
        ),
    ]
