from django.test import TestCase
from .models import Post
from django.urls import reverse
''' it will not affect the actual database it will create a temporary one'''


class PostModelTest(TestCase):

    def setUp(self):
        Post.objects.create(text='just a test')

    def test_text_content(self):
        post = Post.objects.get(id=1)
        expected_object_name = f'{post.text}'
        self.assertEqual(expected_object_name, 'just a test')


class HomePageViewTest(TestCase): # new
    def setUp(self):
        Post.objects.create(text='this is another test')

    def test_view_url_exists_at_proper_location(self):
        resp = self.client.get('/')
        self.assertEqual(resp.status_code, 200)

    def test_view_url_by_name(self):
        resp = self.client.get(reverse('home'))
        self.assertEqual(resp.status_code, 200)

    def test_view_uses_correct_template(self):
        resp = self.client.get(reverse('home'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'home.html')



'''
Found 4 test(s).
Creating test database for alias 'default'...
System check identified no issues (0 silenced).
....
----------------------------------------------------------------------
Ran 4 tests in 0.020s

OK
Destroying test database for alias 'default'...


Why does the output say four tests and not six? The answer is that our setUp methods are not
actually tests, they are helper functions. Only functions that start with the name test* and exist
in a tests.py file will be run as tests when we execute the python manage.py test command
'''