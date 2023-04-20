from django.test import TestCase
from .models import News


class TestNews(TestCase):

    def setUp(self):
        self.news = News.objects.create(title='Новая новость', content='Содержимое новости')
        print('Я выполняюсь перед каждым тестом')

    def tearDown(self):
        News.objects.all().delete()
        print('Я выполняюсь после каждого теста')

    def test_init(self):
        self.assertEqual(self.news.title, 'Новая новость')
        self.assertEqual(self.news.content, 'Содержимое новости')
