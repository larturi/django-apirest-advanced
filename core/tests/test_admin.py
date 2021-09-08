from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from django.urls import reverse


class AdminTests(TestCase):

    def setUp(self):
        self.client = Client()
        self.admin_user = get_user_model().objects.create_superuser(
            email='admintest@test.com',
            password='Aa123456'
        )
        self.client.force_login(self.admin_user)

        self.user = get_user_model().objects.create_user(
            email='usertest@test.com',
            password='Aa123456',
            name='Juan Perez'
        )

    def test_users_listed(self):
        """ Testear que los users has sido listados en la pagina de Users """

        url = reverse('admin:core_user_changelist')
        res = self.client.get(url)

        self.assertContains(res, self.user.name)
        self.assertContains(res, self.user.email)

    def test_edit_user_page(self):
        """ Prueba que la pagina de edición de usuarios funcione """

        url = reverse('admin:core_user_change', args=[self.user.id])
        res = self.client.get(url)

        self.assertEqual(res.status_code, 200)

    def test_create_user_page(self):
        """ Prueba que la pagina de crear usuarios funcione """

        url = reverse('admin:core_user_add')
        res = self.client.get(url)

        self.assertEqual(res.status_code, 200)
