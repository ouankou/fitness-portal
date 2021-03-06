# Generated by Django 2.2.5 on 2019-10-08 17:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Activities',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('category', models.CharField(choices=[('w', 'Weight'), ('c', 'Cardio')], max_length=55)),
                ('reference_material', models.TextField(blank=True, null=True)),
                ('status', models.BooleanField(default=True)),
                ('created_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('purpose', models.CharField(choices=[('cmp', 'Competitive'), ('rec', 'Recreational')], max_length=100)),
                ('starting_weight', models.DecimalField(decimal_places=2, max_digits=5)),
                ('target_weight', models.DecimalField(decimal_places=2, max_digits=5)),
                ('current_weight', models.DecimalField(decimal_places=2, max_digits=5)),
                ('health_issues', models.TextField(blank=True, default='')),
                ('blood_group', models.CharField(max_length=55)),
                ('height_in_feet', models.DecimalField(decimal_places=2, max_digits=5)),
                ('arm_size', models.DecimalField(decimal_places=2, max_digits=5)),
                ('chest_size', models.DecimalField(decimal_places=2, max_digits=5)),
                ('leg_size', models.DecimalField(decimal_places=2, max_digits=5)),
            ],
        ),
        migrations.CreateModel(
            name='Trainer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('applied_on', models.DateField(auto_now_add=True)),
                ('approved_on', models.DateField(auto_now_add=True)),
                ('years_of_previous_experience', models.IntegerField(default=0)),
                ('locations_served', models.TextField(blank=True, default='')),
                ('charge', models.DecimalField(decimal_places=2, max_digits=5)),
                ('certification', models.TextField(default='')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='TrainerRating',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.IntegerField()),
                ('rated_on', models.DateTimeField(auto_now_add=True)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portal.Client')),
                ('trainer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portal.Trainer')),
            ],
        ),
        migrations.CreateModel(
            name='EmergencyContact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('number', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('address', models.TextField()),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portal.Client')),
            ],
        ),
        migrations.AddField(
            model_name='client',
            name='current_trainer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='portal.Trainer'),
        ),
        migrations.AddField(
            model_name='client',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='Challenges',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=55)),
                ('created_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ChallengedActivities',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.BooleanField(default=True)),
                ('activity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portal.Activities')),
                ('challenge', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portal.Challenges')),
            ],
        ),
        migrations.CreateModel(
            name='AssignedChallengesToClient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('routine_type', models.CharField(choices=[('d', 'Daily'), ('w', 'Weekly'), ('m', 'Monthly')], max_length=55)),
                ('start_date', models.DateField(auto_now_add=True)),
                ('end_date', models.DateField(auto_now_add=True)),
                ('assigned_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portal.Trainer')),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portal.Client')),
            ],
        ),
    ]
