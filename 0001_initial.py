from django.db import migrations,models


class Migration(migrations.Migration):
    initial = True

    dependencies =[

    ]
    operations = [
        migrations.CreateModel(
            name = 'Document',
            fields=[
                ('id',models.BigAutoField(auto_created=True,primary_key=True,serialize=False,verbose_name='ID')),
                ('content',models.TextField()),
                ('exit',models.DateTimeField(blank=True, null=True)),
                ('file',models.FileField(upload_to='document/')),
            ]
        )
    ]