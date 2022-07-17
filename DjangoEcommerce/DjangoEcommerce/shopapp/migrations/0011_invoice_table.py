# Generated by Django 4.0.5 on 2022-07-17 20:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('shopapp', '0010_rename_checkout_cart_delivered_cart_delivery_agent_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Invoice_table',
            fields=[
                ('invoice_id', models.AutoField(primary_key=True, serialize=False)),
                ('date_cashout', models.DateTimeField(default=django.utils.timezone.now)),
                ('total_price', models.CharField(max_length=11)),
                ('cashout', models.BooleanField(default=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]