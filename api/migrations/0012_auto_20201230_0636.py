# Generated by Django 3.1.4 on 2020-12-30 09:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0011_auto_20201230_0535'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profissional',
            name='endereco',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='api.endereco'),
        ),
    ]