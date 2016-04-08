from rest_framework.test import APITestCase
from rest_framework import status
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User


class PartsApiTests(APITestCase):

    def setUp(self):
        super(PartsApiTests, self).setUp()

        self.user = User.objects.create_superuser(
            'testuser',
            'test@example.com',
            'test'
        )

    def test_get_parts_list(self):
        self.client.login(username=self.user.username, password='test')

        url = reverse('api:part-list')
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_parts_detail(self):
        self.client.login(username=self.user.username, password='test')

        url = reverse('api:part-detail')
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
