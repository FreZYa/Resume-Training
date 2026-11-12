from django.core import mail
from django.test import TestCase, override_settings
from django.urls import reverse

from contact.models import Message


@override_settings(EMAIL_BACKEND='django.core.mail.backends.locmem.EmailBackend')
class ContactFormTests(TestCase):
    def test_contact_page_renders(self):
        response = self.client.get(reverse('contact'))
        self.assertEqual(response.status_code, 200)

    def test_valid_submission_saves_message_and_sends_email(self):
        response = self.client.post(reverse('contact_form'), {
            'name': 'Test',
            'email': 'test@example.com',
            'subject': 'Hello',
            'message': 'Hi there',
        })
        self.assertTrue(response.json()['success'])
        self.assertEqual(Message.objects.count(), 1)
        self.assertEqual(len(mail.outbox), 1)
        self.assertEqual(mail.outbox[0].reply_to, ['test@example.com'])

    def test_invalid_submission_is_rejected(self):
        response = self.client.post(reverse('contact_form'), {'name': '', 'email': 'bad'})
        self.assertFalse(response.json()['success'])
        self.assertEqual(Message.objects.count(), 0)
        self.assertEqual(len(mail.outbox), 0)
