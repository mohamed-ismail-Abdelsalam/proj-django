# Generated by Django 4.0.5 on 2022-07-07 16:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0003_featured'),
    ]

    operations = [
        migrations.AlterField(
            model_name='featured',
            name='pro',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='fet', to='Users.projects'),
        ),
    ]
