import unittest
import code_file
from unittest.mock import patch

documents = []
directories = {}

def set_up_data():
    # for document in code_file.documents:
    #     documents.append(document)
    # for directory in code_file.directories.keys():
    #     directories[directory] = code_file.directories[directory]
    pass


@patch('code_file.documents', documents, create=True)
@patch('code_file.directories', directories, create=True)
class TestOfDirectoriesApp(unittest.TestCase):

    def setUp(self):
        for document in code_file.documents:
            documents.append(document)
        for directory in code_file.directories.keys():
            directories[directory] = code_file.directories[directory]


    def test_of_add_shelf(self):
        begin_len = len(directories)
        code_file.add_shelf('a')
        end_len = len(directories)
        self.assertLess(begin_len, end_len)

    def test_of_move(self):
        self.assertEqual(len(directories['3']), 0)
        code_file.move('10006', '3')
        self.assertGreater(len(directories['3']), 0)
        self.assertIn('10006', directories['3'])


    def test_of_delete(self):
        docs_length_before = len(documents)
        self.assertIn('10006', directories['2'])
        code_file.delete('10006')
        self.assertNotIn('10006', directories['2'])
        self.assertGreater(docs_length_before, len(documents))


if __name__ == '__main__':
    unittest.main()
