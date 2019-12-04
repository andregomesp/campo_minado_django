from django.db import models

# Create your models here.


class Bomb(models.Model):
    position_x = models.IntegerField(default=0)
    position_y = models.IntegerField(default=0)


class Board(models.Model):
    bombs = models.ForeignKey(Bomb, on_delete=models.CASCADE)

