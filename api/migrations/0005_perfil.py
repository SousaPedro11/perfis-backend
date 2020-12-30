# Generated by Django 3.1.4 on 2020-12-30 06:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_auto_20201230_0323'),
    ]

    operations = [
        migrations.CreateModel(
            name='Perfil',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('profissional', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='api.profissional')),
            ],
            options={
                'verbose_name': 'Perfil',
                'verbose_name_plural': 'Perfis',
                'db_table': 'tbl_perfil',
                'managed': True,
            },
        ),
    ]