# Generated by Django 5.2.4 on 2025-07-12 11:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_remove_repairer_skill_set_alter_repairer_field'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='user_type',
            field=models.CharField(choices=[('admin', 'Admin'), ('customer', 'Customer'), ('repairer', 'Repairer'), ('both', 'Customer and Repairer')], default='customer', max_length=20),
        ),
        migrations.AlterField(
            model_name='repairer',
            name='field',
            field=models.CharField(choices=[('hardware', 'Hardware'), ('software', 'Software')], max_length=20),
        ),
        migrations.AlterField(
            model_name='repairer',
            name='nin',
            field=models.CharField(max_length=20, unique=True),
        ),
        migrations.AlterField(
            model_name='repairer',
            name='verification_id',
            field=models.CharField(max_length=50, unique=True),
        ),
        migrations.AlterField(
            model_name='repairer',
            name='wallet_id',
            field=models.CharField(max_length=50, unique=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='last_login',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='phone',
            field=models.CharField(max_length=15, unique=True),
        ),
    ]
