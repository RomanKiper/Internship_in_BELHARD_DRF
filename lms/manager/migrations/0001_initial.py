# Generated by Django 4.2 on 2023-04-15 21:08

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
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address_name', models.CharField(max_length=64, verbose_name='адрес')),
            ],
            options={
                'verbose_name': 'адрес',
                'verbose_name_plural': 'адреса',
            },
        ),
        migrations.CreateModel(
            name='Audience',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.PositiveSmallIntegerField(verbose_name='номер аудитории')),
                ('is_online', models.BooleanField(default=False, verbose_name='онлайн')),
                ('address', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='manager.address', verbose_name='адрес аудитории')),
            ],
            options={
                'verbose_name': 'аудитория',
                'verbose_name_plural': 'аудитории',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='категория')),
            ],
            options={
                'verbose_name': 'категория',
                'verbose_name_plural': 'категория',
            },
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('duration', models.PositiveSmallIntegerField(verbose_name='продолжительность обучения в днях')),
                ('name', models.CharField(max_length=64, unique=True, verbose_name='название курса')),
                ('price', models.DecimalField(decimal_places=2, max_digits=6, verbose_name='стоимость')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='manager.category', verbose_name='категория')),
            ],
            options={
                'verbose_name': 'курсы',
                'verbose_name_plural': 'курсы',
            },
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.PositiveSmallIntegerField(verbose_name='номер группы')),
                ('date_start', models.DateField(null=True, verbose_name='дата начала')),
                ('audience', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='manager.audience', verbose_name='аудитория')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='manager.course', verbose_name='курс')),
                ('mentor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='ментор')),
            ],
            options={
                'verbose_name': 'группа',
                'verbose_name_plural': 'группы',
            },
        ),
        migrations.CreateModel(
            name='PaymentInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_paid_date', models.DateField(null=True, verbose_name='дата 1-ой оплаты')),
                ('first_paid_amount', models.DecimalField(decimal_places=2, max_digits=6, verbose_name='сумма 1-ой оплаты')),
                ('sec_paid_date', models.DateField(null=True, verbose_name='дата 2-ой оплаты')),
                ('sec_paid_amount', models.DecimalField(decimal_places=2, max_digits=6, verbose_name='сумма 2-ой оплаты')),
            ],
            options={
                'verbose_name': 'статус оплаты',
                'verbose_name_plural': 'статус оплаты',
            },
        ),
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.DateTimeField(verbose_name='дата и время занятия')),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='manager.group', verbose_name='номер группы')),
            ],
            options={
                'verbose_name': 'расписание',
                'verbose_name_plural': 'расписания',
            },
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=50, verbose_name='описание задачи')),
                ('doc', models.CharField(max_length=1024, verbose_name='материалы по задаче')),
                ('day', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='manager.schedule', verbose_name='дата и время занятия')),
            ],
            options={
                'verbose_name': 'задача',
                'verbose_name_plural': 'задачи',
            },
        ),
        migrations.CreateModel(
            name='GroupUsers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group', models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='manager.group', verbose_name='номер группы')),
                ('user', models.ForeignKey(default='Иванов', on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='студент')),
            ],
            options={
                'verbose_name': 'группа-юзер',
                'verbose_name_plural': 'группа-юзер',
            },
        ),
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=350, null=True, verbose_name='отзыв')),
                ('is_published', models.BooleanField(default=False, verbose_name='опубликовано')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='пользователь')),
            ],
            options={
                'verbose_name': 'отзывы',
                'verbose_name_plural': 'отзывы',
            },
        ),
    ]