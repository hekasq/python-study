import unittest

from document_parser.main.parser import for_test


class ParserTest(unittest.TestCase):

    def test_timestamps(self):
        self.assertTrue(for_test(), 1)
