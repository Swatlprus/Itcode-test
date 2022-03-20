from django.test import TestCase, Client
from django.urls import reverse

from core import models

class CompanyModel(TestCase):

    def setUp(self):
        self.book = models.Company.objects.create(name='Test Company')

    def testStr(self):
        self.assertEqual(
            str(self.book),
            'Test Company', 'Строковое представление объекта должно возвращать название'
        )

class CompanySearchTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.book1 = models.Company.objects.create(name='Test Company 1')
        self.book2 = models.Company.objects.create(name='Test Company 2')

    def testWithoutParams(self):
        response = self.client.get(reverse('core:company_list'))
        self.assertEqual(200, response.status_code)
        self.assertSequenceEqual(
            list(response.context['object_list']),
            list(models.Company.objects.all()),
            'При поиске без параметров должны выводиться все компании',
        )

    def testSearchByName(self):
        response = self.client.get(reverse('core:company_list'), data={'name': 'Test Company 1'})
        self.assertEqual(1, response.context['object_list'].count())
        self.assertEqual(
            'Test Company 1',
            response.context['object_list'].first().name,
        )