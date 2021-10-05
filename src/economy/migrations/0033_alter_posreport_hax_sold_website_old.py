# Generated by Django 3.2.7 on 2021-10-03 11:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("economy", "0032_rename_hax_sold_website_posreport_hax_sold_website_old"),
    ]

    operations = [
        migrations.AlterField(
            model_name="posreport",
            name="hax_sold_website_old",
            field=models.PositiveIntegerField(
                default=0,
                help_text="The number of HAX sold through webshop tickets being used in the POS. Not used anymore.",
            ),
        ),
    ]