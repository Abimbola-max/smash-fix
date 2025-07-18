# Generated by Django 5.2.4 on 2025-07-13 02:02

import cloudinary.models
import django.db.models.deletion
import django.utils.timezone
import uuid
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='RepairJob',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('device_brand', models.CharField(max_length=100)),
                ('device_model', models.CharField(max_length=100)),
                ('issue_description', models.TextField()),
                ('budget', models.DecimalField(decimal_places=2, max_digits=10)),
                ('status', models.CharField(choices=[('open', 'Open'), ('bidding', 'Bidding'), ('assigned', 'Assigned'), ('in_progress', 'In Progress'), ('repaired', 'Repaired'), ('cancelled', 'Cancelled')], default='open', max_length=20)),
                ('image', cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True, verbose_name='media')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('bid_deadline', models.DateTimeField(default=django.utils.timezone.now)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='jobs', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
