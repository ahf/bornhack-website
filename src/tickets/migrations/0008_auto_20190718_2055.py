# Generated by Django 2.2.2 on 2019-07-18 18:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0007_save_token_to_db'),
    ]

    operations = [
        migrations.RenameField(
            model_name='discountticket',
            old_name='checked_in',
            new_name='used',
        ),
        migrations.RenameField(
            model_name='shopticket',
            old_name='checked_in',
            new_name='used',
        ),
        migrations.RenameField(
            model_name='sponsorticket',
            old_name='checked_in',
            new_name='used',
        ),
        migrations.AlterField(
            model_name='discountticket',
            name='token',
            field=models.CharField(max_length=64),
        ),
        migrations.AlterField(
            model_name='shopticket',
            name='token',
            field=models.CharField(max_length=64),
        ),
        migrations.AlterField(
            model_name='sponsorticket',
            name='token',
            field=models.CharField(max_length=64),
        ),
    ]
