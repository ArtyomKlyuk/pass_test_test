from django.db import models


class Question(models.Model):
    id = models.IntegerField(primary_key=True)
    question_title = models.CharField(verbose_name='Заголовок вопроса', )
    question_body = models.CharField(verbose_name='Тело вопроса')
    max_answer_value = models.IntegerField(verbose_name='Максимальное количество баллов')


class Answer(models.Model):
    question_id = models.ForeignKey(to=Question, on_delete=models.CASCADE)
    answer = models.IntegerField(verbose_name='Ответ')


class Result(models.Model):
    id = models.IntegerField(primary_key=True)
    result = models.IntegerField(verbose_name='Результат')

