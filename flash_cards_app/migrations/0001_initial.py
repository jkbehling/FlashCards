# Generated by Django 3.2.8 on 2022-11-13 03:57

from django.db import migrations, models
import django.db.models.deletion
import django_quill.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Deck',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('card_num', models.IntegerField()),
                ('front', models.CharField(max_length=300)),
                ('front_content', django_quill.fields.QuillField()),
                ('back', models.CharField(max_length=300)),
                ('back_content', django_quill.fields.QuillField()),
                ('card_image', models.ImageField(upload_to='upload/')),
                ('deck', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='flash_cards_app.deck')),
            ],
        ),
    ]