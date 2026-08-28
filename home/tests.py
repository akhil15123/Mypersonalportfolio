from django.core import mail
from django.test import TestCase, override_settings
from django.urls import reverse


class PortfolioViewTests(TestCase):
    def test_home_renders_without_blog_posts(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

    def test_projects_page_renders(self):
        response = self.client.get(reverse('projects'))
        self.assertEqual(response.status_code, 200)

    def test_empty_search_is_safe(self):
        response = self.client.get(reverse('search'))
        self.assertEqual(response.status_code, 200)

    @override_settings(EMAIL_BACKEND='django.core.mail.backends.locmem.EmailBackend')
    def test_valid_contact_sends_email(self):
        response = self.client.post(
            reverse('contact'),
            {
                'name': 'Ada Rivera',
                'email': 'ada@example.com',
                'phone': '4045550100',
                'message': 'I would like to discuss a Python project.',
            },
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(mail.outbox), 1)
