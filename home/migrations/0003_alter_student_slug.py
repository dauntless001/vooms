# Generated by Django 4.2.1 on 2023-06-07 21:07

from django.db import migrations, models
import voomsdb.utils.strings


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0002_student_published_student_slug"),
    ]

    operations = [
        migrations.AlterField(
            model_name="student",
            name="slug",
            field=models.SlugField(
                blank=True, default=voomsdb.utils.strings.generate_ref_no, null=True
            ),
        ),
    ]
