# Generated by Django 5.2 on 2025-04-12 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0003_alter_project_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('What I Do', models.TextField(help_text='Describe what you do and your professional background.')),
                ('Core Skills', models.TextField(help_text='List your core skills and areas of expertise. Use markdown for formatting.')),
            ],
        ),
    ]
