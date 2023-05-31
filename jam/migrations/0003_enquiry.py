# Generated by Django 4.1 on 2022-08-30 12:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jam', '0002_employer'),
    ]

    operations = [
        migrations.CreateModel(
            name='Enquiry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('gender', models.CharField(max_length=6)),
                ('address', models.TextField()),
                ('contactno', models.CharField(max_length=50)),
                ('emailaddress', models.EmailField(max_length=50)),
                ('enquirytext', models.TextField()),
                ('posteddate', models.CharField(max_length=30)),
            ],
        ),
    ]
