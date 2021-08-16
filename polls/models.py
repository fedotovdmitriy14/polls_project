from django.db import models


class Poll(models.Model):
    poll_title = models.CharField(max_length=64)
    description = models.TextField(default='poll')
    start_date = models.DateField(default='2021-08-08')
    end_date = models.DateField(default='2021-12-12')

    def __str__(self):
        return self.poll_title

class Question(models.Model):

    poll_id = models.ForeignKey(Poll, on_delete=models.CASCADE, related_name='questions')
    questions = models.CharField(max_length=256)
    question_type = models.CharField(max_length=256)

    def __str__(self):
        return self.questions

class Choice(models.Model):
    question = models.ForeignKey(Question, related_name='choices', on_delete=models.CASCADE)
    text = models.CharField(max_length=64)

    def __str__(self):
        return self.text


class Answer(models.Model):
    user_id = models.IntegerField()
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE, related_name='poll')
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='question')
    choice = models.ForeignKey(Choice, on_delete=models.CASCADE, related_name='choice', null=True)
    choice_text = models.CharField(max_length=300, null=True)

    def __str__(self):
        return self.choice_text
