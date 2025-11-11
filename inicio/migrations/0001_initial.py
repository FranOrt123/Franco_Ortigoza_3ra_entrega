from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Camiseta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('talle', models.CharField(max_length=5)),
                ('modelo', models.CharField(max_length=100)),
                ('club', models.CharField(max_length=50)),
            ],
        ),
    ]
