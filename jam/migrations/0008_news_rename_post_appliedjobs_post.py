# Generated by Django 4.1 on 2022-09-05 10:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jam', '0007_appliedjobs'),
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('newstext', models.TextField()),
                ('newsdate', models.CharField(max_length=30)),
            ],
        ),
        migrations.RenameField(
            model_name='appliedjobs',
            old_name='Post',
            new_name='post',
        ),
    ]