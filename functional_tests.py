from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):

	def setUp(self):
		self.browser = webdriver.Firefox()
		self.browser.implicitly_wait(3)

	def tearDown(self):
		self.browser.quit()

	def test_can_start_a_list_and_retrieve_it_later(self):
# James wants to start a to-do list and go to this website to do so
		self.browser.get('http://localhost:8000')

# He noticies he is in a to-do list web page by its title
		self.assertIn('To-Do', self.browser.title)
		self.fail('Finish the test!')

# He is invited to add a new item to a list

# He types "Reserve Paris rugby match ticket" 'cause he loves rugby

# He hits enter and the page shows
# "1: Reserver Paris rugby match ticket" as an item in the list

# There is still a text box inviting to write a new item
# He enters "Reserve hotel in paris"
	
# The page updates and show both items

# He wonders if still be able to se the list when he closes his browser
# The list has generated a unique URL - and an explanatory message about it 

# He visits the URL - the list is still there

# Satisfied, he goes to sleep

if __name__ == '__main__':
	unittest.main(warnings='ignore')

