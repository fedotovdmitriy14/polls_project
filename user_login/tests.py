from django.conf import settings
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)


class LoginLogout(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(username="testSubject", password="12345")

    def test_login(self):
        data = {
            "username": "testSubject",
            "password": "12345"
        }
        response = self.client.post(reverse("login"), data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_logout(self):
        self.token = Token.objects.get(user__username="testSubject")
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        response = self.client.post(reverse('logout'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)



