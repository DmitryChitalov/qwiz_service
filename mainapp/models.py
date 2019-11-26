from django.db import models
from datetime import date


class SampleGame(models.Model):
    name = models.CharField(max_length=32, verbose_name='game name')
    image = models.ImageField(upload_to='image min', blank=True)
    image_big = models.ImageField(upload_to='image big', blank=True)
    date = models.DateField(verbose_name='date: xx.xx.xxxx')
    time = models.TimeField(verbose_name='time: xx:xx')
    place = models.CharField(max_length=64, verbose_name='place')
    description = models.TextField(max_length=512, blank=True, verbose_name='description')
    # active = models.BooleanField(default=True, verbose_name='is active')

    def __str__(self):
        if self.date > date.today():
            return f'{self.date} {self.time}'
        return f'* {self.date} {self.time}'



class SampleCommand(models.Model):
    name = models.CharField(max_length=32, unique=True, verbose_name='name')
    # game = models.ForeignKey(SampleGame, verbose_name='game', on_delete=models.CASCADE)
    points = models.IntegerField(default=0, verbose_name='points')
    active = models.BooleanField(default=False, verbose_name='is active')


class ComingRequests(models.Model):
    MEMEBERS = (
        ('1', '1 участник'),
        ('2', '2 участника'),
        ('3', '3 участника'),
        ('4', '4 участника'),
        ('5', '5 участников'),
        ('6', '6 участников'),
        ('7', '7 участников'),
        ('8', '8 участников'),
        ('9', '9 участников'),
        ('10', '10 участников'),
    )
    mail = models.CharField(max_length=32, verbose_name='e-mail')
    phone = models.CharField(max_length=16, verbose_name='телефон')
    command_name = models.CharField(max_length=32, verbose_name='название команды')
    capitan_name = models.CharField(max_length=32, verbose_name='имя капитана')
    members = models.CharField(max_length=16, choices=MEMEBERS, verbose_name='количество участников')
    game = models.ForeignKey(SampleGame, verbose_name='Дата', on_delete=models.CASCADE)


class SampleQwiz(models.Model):
    name = models.CharField(max_length=32, verbose_name='name')
    description = models.TextField(max_length=256, blank=True, verbose_name='description')
    active = models.BooleanField(default=False, verbose_name='is active')

    def __str__(self):
        return self.name


class Qwestions(models.Model):
    ANSWERS = (('a', 'a'), ('b', 'b'), ('c', 'c'), ('d', 'd'))
    theme = models.ForeignKey(SampleQwiz, verbose_name='theme', on_delete=models.CASCADE)
    qwestion = models.CharField(max_length=128, verbose_name='qwestion')
    answer_a = models.CharField(max_length=64, verbose_name='answer_a')
    point_a = models.IntegerField(default=0, verbose_name='points_a')
    answer_b = models.CharField(max_length=64, verbose_name='answer_b')
    point_b = models.IntegerField(default=0, verbose_name='points_b')
    answer_c = models.CharField(max_length=64, verbose_name='answer_c')
    point_c = models.IntegerField(default=0, verbose_name='points_c')
    answer_d = models.CharField(max_length=64, verbose_name='answer_d')
    point_d = models.IntegerField(default=0, verbose_name='points_d')

    def to_json(self):
        return {
            'qwestion': self.qwestion,
            'a': self.answer_a,
            'b': self.answer_b,
            'c': self.answer_c,
            'd': self.answer_d,
            'p_a': self.point_a,
            'p_b': self.point_b,
            'p_c': self.point_c,
            'p_d': self.point_d,
        }
