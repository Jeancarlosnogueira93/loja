# Generated by Django 5.0 on 2023-12-17 15:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contas', '0002_transacao'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='transacao',
            options={'verbose_name_plural': 'Trasações'},
        ),
        migrations.AlterField(
            model_name='transacao',
            name='obs',
            field=models.TextField(blank=True, null=True),
        ),
    ]
