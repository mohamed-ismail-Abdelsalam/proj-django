# Generated by Django 4.0.5 on 2022-06-27 21:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0008_alter_project_coverimage_alter_project_image1_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='coverimage',
            field=models.ImageField(upload_to='images'),
        ),
        migrations.AlterField(
            model_name='project',
            name='image1',
            field=models.ImageField(upload_to='images'),
        ),
        migrations.AlterField(
            model_name='project',
            name='image2',
            field=models.ImageField(upload_to='images'),
        ),
        migrations.AlterField(
            model_name='project',
            name='image3',
            field=models.ImageField(upload_to='images'),
        ),
        migrations.AlterField(
            model_name='project',
            name='image4',
            field=models.ImageField(upload_to='images'),
        ),
    ]
