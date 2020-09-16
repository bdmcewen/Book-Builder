from django.test import SimpleTestCase, TestCase


class ViewTests(SimpleTestCase):

    def test_view_index(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed('index.html')

    def test_view_no_page(self):
        response = self.client.get('/home.html')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed('home.html')

    def test_view_missing_template(self):
        response = self.client.get('/xxx')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed('missing.html')

    def test_view_bad_url(self):
        response = self.client.get('/xxx/home.html')
        self.assertEqual(response.status_code, 404)
        self.assertTemplateUsed('missing.html')
