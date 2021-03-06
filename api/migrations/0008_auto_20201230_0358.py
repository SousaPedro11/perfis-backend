# Generated by Django 3.1.4 on 2020-12-30 06:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_auto_20201230_0357'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pessoacurso',
            old_name='curso_id',
            new_name='curso',
        ),
        migrations.RenameField(
            model_name='pessoacurso',
            old_name='profissional_id',
            new_name='profissional',
        ),
        migrations.AlterUniqueTogether(
            name='pessoacurso',
            unique_together={('profissional', 'curso')},
        ),
    ]
