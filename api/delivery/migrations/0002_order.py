from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('delivery', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=5)),
                (
                    'status',
                    models.PositiveSmallIntegerField(
                        choices=[(1, 'CREATED'), (2, 'PREPARING'), (3, 'ON_THE_WAY'), (4, 'DELIVERED')]
                    )
                ),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('items', models.ManyToManyField(to='delivery.MenuItem')),
                (
                    'restaurant',
                    models.ForeignKey(on_delete=models.deletion.CASCADE, to='delivery.restaurant')
                ),
                ('user', models.ForeignKey(on_delete=models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
