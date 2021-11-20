from django.conf import settings
from django.db import migrations, models
from django.core.validators import MinValueValidator
from django.db.models.deletion import CASCADE


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ('delivery', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.PositiveSmallIntegerField(validators=[MinValueValidator(1)])),
                ('menu_item', models.ForeignKey(on_delete=CASCADE, to='delivery.menuitem')),
            ],
        ),
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
                ('items', models.ManyToManyField(to='order.OrderItem')),
                ('restaurant', models.ForeignKey(on_delete=CASCADE, to='delivery.restaurant')),
                ('user', models.ForeignKey(on_delete=CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]