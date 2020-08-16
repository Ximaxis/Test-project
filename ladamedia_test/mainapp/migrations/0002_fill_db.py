# Generated by Django 2.2.12 on 2020-05-17 12:42

from django.db import migrations
from django.utils.text import slugify

def forwards_func(apps, schema_editor):
    head_model = apps.get_model("mainapp", "OrderHeaders")
    detail_model = apps.get_model("mainapp", "OrderDetails")

    head_obj = head_model.objects.create(
        pk=1,
        reg_number="NWMX23214JJ",
    )
    detail_model.objects.create(
        pk=1,
        hdr=head_obj,
        good_id=1,
        amount=12412,
        price=412.24
    )
    detail_model.objects.create(
        pk=2,
        hdr=head_obj,
        good_id=2,
        amount=15125.3644,
        price=6412.13
    )
    detail_model.objects.create(
        pk=3,
        hdr=head_obj,
        good_id=3,
        amount=112412.22,
        price=6412.13
    )
    detail_model.objects.create(
        pk=4,
        hdr=head_obj,
        good_id=4,
        amount=76512.2622,
        price=1212.13
    )

    del head_obj
    head_obj = head_model.objects.create(
        pk=2,
        reg_number="NSDKW241411",
    )
    detail_model.objects.create(
        pk=5,
        hdr=head_obj,
        good_id=5,
        amount=45742.5822,
        price=24412.13
    )

    detail_model.objects.create(
        pk=6,
        hdr=head_obj,
        good_id=6,
        amount=68662.7822,
        price=36412.13
    )
    detail_model.objects.create(
        pk=7,
        hdr=head_obj,
        good_id=7,
        amount=88662.7822,
        price=76412.13
    )

    detail_model.objects.create(
        pk=8,
        hdr=head_obj,
        good_id=1,
        amount=46412,
        price=412.24
    )
    del head_obj

    head_obj = head_model.objects.create(
        pk=3,
        reg_number="DJWIOR784268",
    )
    detail_model.objects.create(
        pk=9,
        hdr=head_obj,
        good_id=8,
        amount=15,
        price=4
    )
    detail_model.objects.create(
        pk=10,
        hdr=head_obj,
        good_id=9,
        amount=4,
        price=15
    )

    del head_obj


def reverse_func(apps, schema_editor):
    head_model = apps.get_model("mainapp", "OrderHeaders")
    head_model.objects.all().delete()


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0001_initial'),
    ]

    operations = [migrations.RunPython(forwards_func, reverse_func)]