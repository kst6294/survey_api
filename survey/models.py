from django.db import models

from core.models import BaseModel, User


class Survey(BaseModel):
    title = models.CharField(max_length=50)
    
    class Meta:
        db_table = "surveys"

    def __str__(self):
        return self.title


class Question(models.Model):
    title  = models.CharField(max_length=100)
    survey = models.ForeignKey(Survey, on_delete=models.PROTECT, related_name='question')

    class Meta:
        db_table = "questions"

    def __str__(self):
        return self.title


class Answer(models.Model):
    user     = models.ForeignKey(User, on_delete=models.PROTECT)
    content  = models.CharField(max_length=100)
    question = models.ForeignKey(Question, on_delete=models.PROTECT, related_name='answers')

    class Meta:
        db_table = "answers"

    def __str__(self):
        return self.content


