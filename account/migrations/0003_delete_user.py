# Generated by Django 4.1.5 on 2023-02-16 16:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0004_bookpost_sell_price_alter_bookcomment_user_and_more"),
        ("account", "0002_profile"),
    ]

    operations = [
        migrations.DeleteModel(
            name="User",
        ),
    ]