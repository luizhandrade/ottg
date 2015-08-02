from django.core.urlresolvers import resolve
from django.test import TestCase
from django.http import HttpRequest
from django.template.loader import render_to_string
from lists.views import home_page


# Create your tests here.
class HomePageTest(TestCase):

    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)

    def test_home_page_returns_correct_hmtl(self):
        request = HttpRequest()
        response = home_page(request)
        #self.assertTrue(response.content.startswith(b'<html'))
        #self.assertIn(b'<title>To-Do lists</title>', response.content)
        #self.assertTrue(response.content.strip().endswith(b'</html>'))
        expected_html = render_to_string('home.html')
        self.assertEqual(response.content.decode(), expected_html)

    def test_home_can_save_a_POST_request(self):
# Prepare request
        request = HttpRequest()
# Define method
        request.method = 'POST'
# Post new item
        request.POST['item_text'] = 'A new list item'

# Get response back
        response = home_page(request)
# Test it! :)
        self.assertIn('A new list item', response.content.decode())

        expected_html = render_to_string(
            'home.html',
            {'new_item_text': 'A new list item'}
        )
        self.assertEqual(response.content.decode(), expected_html)
