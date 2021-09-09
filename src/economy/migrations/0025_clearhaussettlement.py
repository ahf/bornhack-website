# Generated by Django 3.2.7 on 2021-09-07 16:29

import uuid

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("economy", "0024_epaytransaction"),
    ]

    operations = [
        migrations.CreateModel(
            name="ClearhausSettlement",
            fields=[
                (
                    "uuid",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("created", models.DateTimeField(auto_now_add=True)),
                ("updated", models.DateTimeField(auto_now=True)),
                (
                    "merchant_id",
                    models.IntegerField(
                        help_text="The merchant ID in Clearhaus systems"
                    ),
                ),
                (
                    "merchant_name",
                    models.CharField(
                        help_text="The merchant name in Clearhaus systems",
                        max_length=255,
                    ),
                ),
                (
                    "clearhaus_uuid",
                    models.UUIDField(
                        help_text="The Clearhaus UUID for this settlement."
                    ),
                ),
                (
                    "settled",
                    models.BooleanField(
                        help_text="True if the settlement has been paid out, False if not."
                    ),
                ),
                (
                    "currency",
                    models.CharField(
                        help_text="The currency of this settlement.", max_length=3
                    ),
                ),
                (
                    "period_start_date",
                    models.DateField(
                        help_text="The first date of the period this settlement covers."
                    ),
                ),
                (
                    "period_end_date",
                    models.DateField(
                        blank=True,
                        help_text="The final date of the period this settlement covers. Can be empty if the period is still ongoing.",
                        null=True,
                    ),
                ),
                (
                    "payout_amount",
                    models.DecimalField(
                        blank=True,
                        decimal_places=2,
                        help_text="The amount that was paid out in this settlement. Can be empty if the settlement has not been paid out yet.",
                        max_digits=12,
                        null=True,
                    ),
                ),
                (
                    "payout_date",
                    models.DateField(
                        blank=True,
                        help_text="The date this settlement was paid out.",
                        null=True,
                    ),
                ),
                (
                    "summary_sales",
                    models.DecimalField(
                        decimal_places=2,
                        help_text="The summary sales for this period",
                        max_digits=12,
                    ),
                ),
                (
                    "summary_credits",
                    models.DecimalField(
                        decimal_places=2,
                        help_text="The summary credits for this period",
                        max_digits=12,
                    ),
                ),
                (
                    "summary_refunds",
                    models.DecimalField(
                        decimal_places=2,
                        help_text="The summary refunds for this period",
                        max_digits=12,
                    ),
                ),
                (
                    "summary_chargebacks",
                    models.DecimalField(
                        decimal_places=2,
                        help_text="The summary chargebacks for this period",
                        max_digits=12,
                    ),
                ),
                (
                    "summary_fees",
                    models.DecimalField(
                        decimal_places=2,
                        help_text="The summary fees for this period",
                        max_digits=12,
                    ),
                ),
                (
                    "summary_other_postings",
                    models.DecimalField(
                        decimal_places=2,
                        help_text="The summary other postings for this period",
                        max_digits=12,
                    ),
                ),
                (
                    "summary_net",
                    models.DecimalField(
                        decimal_places=2,
                        help_text="The summary net (total) for this period",
                        max_digits=12,
                    ),
                ),
                (
                    "reserve_amount",
                    models.DecimalField(
                        blank=True,
                        decimal_places=2,
                        help_text="The amount that has been reserved for later payout. Can be empty if nothing has been reserved for this period.",
                        max_digits=12,
                        null=True,
                    ),
                ),
                (
                    "reserve_date",
                    models.DateField(
                        blank=True,
                        help_text="The date the reserve for this period will be paid out.",
                        null=True,
                    ),
                ),
                (
                    "fees_sales",
                    models.DecimalField(
                        decimal_places=2,
                        help_text="The fees for sales for this period",
                        max_digits=12,
                    ),
                ),
                (
                    "fees_refunds",
                    models.DecimalField(
                        decimal_places=2,
                        help_text="The fees for refunds for this period",
                        max_digits=12,
                    ),
                ),
                (
                    "fees_authorisations",
                    models.DecimalField(
                        decimal_places=2,
                        help_text="The fees for authorisations for this period",
                        max_digits=12,
                    ),
                ),
                (
                    "fees_credits",
                    models.DecimalField(
                        decimal_places=2,
                        help_text="The fees for credits for this period",
                        max_digits=12,
                    ),
                ),
                (
                    "fees_minimum_processing",
                    models.DecimalField(
                        decimal_places=2,
                        help_text="The fees for minimum processing for this period",
                        max_digits=12,
                    ),
                ),
                (
                    "fees_service",
                    models.DecimalField(
                        decimal_places=2,
                        help_text="The fees for service for this period",
                        max_digits=12,
                    ),
                ),
                (
                    "fees_wire_transfer",
                    models.DecimalField(
                        decimal_places=2,
                        help_text="The fees for wire transfers for this period",
                        max_digits=12,
                    ),
                ),
                (
                    "fees_chargebacks",
                    models.DecimalField(
                        decimal_places=2,
                        help_text="The fees for chargebacks for this period",
                        max_digits=12,
                    ),
                ),
                (
                    "fees_retrieval_requests",
                    models.DecimalField(
                        decimal_places=2,
                        help_text="The fees for retrieval requests for this period",
                        max_digits=12,
                    ),
                ),
                (
                    "payout_reference_number",
                    models.BigIntegerField(
                        blank=True,
                        help_text="The Clearhaus reference number for the payout of this settlement. Can be empty if the settlement has not been paid out yet.",
                        null=True,
                    ),
                ),
                (
                    "payout_descriptor",
                    models.CharField(
                        blank=True,
                        help_text="The Clearhaus descriptor for the payout of this settlement. Can be empty if the settlement has not been paid out yet.",
                        max_length=100,
                        null=True,
                    ),
                ),
                (
                    "reserve_reference_number",
                    models.BigIntegerField(
                        blank=True,
                        help_text="The Clearhaus reference number for the payout of the reserve of this settlement. Can be empty if there is no reserve or it the reserve has not been paid out yet.",
                        null=True,
                    ),
                ),
                (
                    "reserve_descriptor",
                    models.CharField(
                        blank=True,
                        help_text="The Clearhaus descriptor for the payout of the reserve of this settlement. Can be empty if the settlement has no reserve, or the reserve has not been paid out yet.",
                        max_length=100,
                        null=True,
                    ),
                ),
                (
                    "fees_interchange",
                    models.DecimalField(
                        decimal_places=2,
                        help_text="The fees for interchange for this period",
                        max_digits=12,
                    ),
                ),
                (
                    "fees_scheme",
                    models.DecimalField(
                        decimal_places=2,
                        help_text="The fees for scheme for this period",
                        max_digits=12,
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
    ]
