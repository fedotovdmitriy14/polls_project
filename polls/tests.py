from django.conf import settings
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from . import models

#

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)


class PollsTests(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(username="testUser", password="12345")
        self.token = Token.objects.get(user__username="testUser")
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

        self.poll = models.Poll.objects.create(poll_title="Test", description="test")
        self.question = models.Question.objects.create(poll_id=self.poll, questions="What is your name?",
                                                         question_type='text')
        self.choice = models.Choice.objects.create(question=self.question, text='America')

    def test_pollCreate(self):
        data = {
            "poll_title": "Test Poll",
            "description": "test description",
        }
        response = self.client.post(reverse("polls-list"), data, format="json")
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


    def test_pollList(self):
        response = self.client.get(reverse("polls-list"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_pollDetail(self):
        response = self.client.get(reverse("polls-detail", args=(self.poll.id,)))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_questionCreate(self):
        data = {
            "questions": "Where are you from?",
            "question_type": "text",
            'poll_id': self.poll.id
        }
        response = self.client.post(reverse("questions-list"), data, format="json")
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


    def test_questionList(self):
        response = self.client.get(reverse("questions-list"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_questionDetail(self):
        response = self.client.get(reverse("questions-detail", args=(self.question.id,)))
        self.assertEqual(response.status_code, status.HTTP_200_OK)


    def test_choiceCreate(self):
        data = {
            "question": self.question.id,
            "text": 'USA',
        }
        response = self.client.post(reverse("choices-list"), data, format="json")
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


    def test_choiceList(self):
        response = self.client.get(reverse("choices-list"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_choiceDetail(self):
        response = self.client.get(reverse("choices-detail", args=(self.choice.id,)))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
