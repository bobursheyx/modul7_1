# Generated by Django 5.0.4 on 2024-05-25 18:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='books',
            name='audio',
            field=models.FileField(blank=True, null=True, upload_to='audios'),
        ),
    ]