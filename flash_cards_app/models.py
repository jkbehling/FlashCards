from django.db import models
from django_quill.fields import QuillField

# Create your models here.
class Deck(models.Model):
    name = models.CharField(max_length=300)


class Card(models.Model):
    card_num = models.IntegerField()
    front = models.CharField(max_length=300)
    front_content = QuillField()
    back = models.CharField(max_length=300)
    back_content = QuillField()
    card_image = models.ImageField(upload_to = 'upload/')
    deck = models.ForeignKey(Deck, on_delete=models.CASCADE)

    displayFirst = ""