from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('followers', '0002_auto_20201010_2249'),
    ]

    operations = [
        migrations.AlterField(
            model_name='follower',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
