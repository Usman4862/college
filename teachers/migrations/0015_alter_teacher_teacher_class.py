# Generated by Django 4.1.7 on 2023-02-21 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teachers', '0014_alter_teacher_teacher_class'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='teacher_class',
            field=models.CharField(choices=[('ICS-P1', 'ICS-PART1'), ('NM-P2', 'NON-MEDICAL-PART2'), ('ICS-P2', 'ICS-PART2'), ('M-P1', 'MEDICAL-PART1'), ('NM-P1', 'NON-MEDICAL-PART2'), ('M-P2', 'MEDICAL-PART2')], max_length=10),
        ),
    ]
