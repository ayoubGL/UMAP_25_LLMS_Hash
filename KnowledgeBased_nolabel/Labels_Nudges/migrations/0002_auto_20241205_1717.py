# Generated by Django 3.2.6 on 2024-12-05 16:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Labels_Nudges', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='evaluatechoices',
            name='effectiveness',
            field=models.CharField(choices=[(None, ''), ('Strongly_Disagree', 'Strongly Disagree'), ('Disagree', 'Disagree'), ('Neutral', 'Neutral'), ('Agree', 'Agree'), ('Strongly_Agree', 'Strongly Agree')], default=None, max_length=100, verbose_name='effectiveness'),
        ),
        migrations.AddField(
            model_name='evaluatechoices',
            name='nudge_eval',
            field=models.CharField(choices=[(None, ''), ('Strongly_Disagree', 'Strongly Disagree'), ('Disagree', 'Disagree'), ('Neutral', 'Neutral'), ('Agree', 'Agree'), ('Strongly_Agree', 'Strongly Agree')], default=None, max_length=100, verbose_name='persuasiveness'),
        ),
        migrations.AddField(
            model_name='evaluatechoices',
            name='understandability',
            field=models.CharField(choices=[(None, ''), ('Strongly_Disagree', 'Strongly Disagree'), ('Disagree', 'Disagree'), ('Neutral', 'Neutral'), ('Agree', 'Agree'), ('Strongly_Agree', 'Strongly Agree')], default=None, max_length=100, verbose_name='understandability'),
        ),
    ]
