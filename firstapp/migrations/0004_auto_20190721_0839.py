# Generated by Django 2.2.3 on 2019-07-21 08:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0003_auto_20190721_0839'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Mark',
            new_name='Marks',
        ),
        migrations.AlterField(
            model_name='marks',
            name='rollNo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='result', to='firstapp.Student'),
        ),
    ]
