# Generated by Django 2.0.2 on 2019-01-13 13:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('operations', '0004_auto_20180220_1434'),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('balance', models.DecimalField(decimal_places=2, max_digits=10)),
                ('name', models.CharField(max_length=256)),
                ('description', models.CharField(max_length=256, null=True)),
                ('owned_by', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('account_balance_pre', models.DecimalField(decimal_places=2, max_digits=10)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('account_balance_post', models.DecimalField(decimal_places=2, max_digits=10)),
                ('description', models.CharField(max_length=256)),
                ('affected_account', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='operations.Account')),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.RemoveField(
            model_name='purchase',
            name='purchase_id',
        ),
        migrations.RemoveField(
            model_name='purchase',
            name='user_id',
        ),
        migrations.AddField(
            model_name='purchase',
            name='product_total',
            field=models.DecimalField(decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='purchase',
            name='product_amount',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='purchase',
            name='product_price',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
        migrations.AddField(
            model_name='bbsuser',
            name='default_account',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='operations.Account'),
        ),
        migrations.AddField(
            model_name='purchase',
            name='transaction_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='operations.Transaction'),
        ),
    ]
