from django.test import SimpleTestCase


class SimpleTests(SimpleTestCase):
    def test_home_page_status_code(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_about_page_status_code(self):
        response = self.client.get('/about/')
        self.assertEqual(response.status_code, 200)


# on the command line type 'python manage.py test' to execute all functions in this class

'''
if you get an output like that
System check identified no issues (0 silenced).
..
----------------------------------------------------------------------
Ran 2 tests in 0.016s

OK
then you are ok
'''
