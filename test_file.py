import unittest
from copy import deepcopy
import code_file
from unittest.mock import patch


#@patch('code_file.documents', documents, create=True)
#@patch('code_file.directories', directories, create=True)
class TestOfDirectoriesApp(unittest.TestCase):

    def setUp(self):
        self.directories = deepcopy(code_file.directories)
        self.documents = deepcopy(code_file.documents)

    def test_of_add_shelf(self):
        begin_len = len(self.directories)
        with patch('code_file.documents', self.documents), \
             patch('code_file.directories', self.directories):
            code_file.add_shelf('a')
        end_len = len(self.directories)
        self.assertLess(begin_len, end_len)

    def test_of_move(self):
        self.assertEqual(len(self.directories['3']), 0)
        with patch('code_file.documents', self.documents), \
             patch('code_file.directories', self.directories):
            code_file.move('10006', '3')
        self.assertGreater(len(self.directories['3']), 0)
        self.assertIn('10006', self.directories['3'])


    def test_of_delete(self):
        docs_length_before = len(self.documents)
        self.assertIn('10006', self.directories['2'])
        with patch('code_file.documents', self.documents), \
             patch('code_file.directories', self.directories):
            code_file.delete('10006')
        self.assertNotIn('10006', self.directories['2'])
        self.assertGreater(docs_length_before, len(self.documents))


if __name__ == '__main__':
    unittest.main()
