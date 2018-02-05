#!/usr/bin/python
# -*- coding: utf-8 -*-

import unittest
from bs4 import BeautifulSoup
from html_table_extractor.extractor import Extractor


class TestSimpleExtractor(unittest.TestCase):
    def setUp(self):
        html = """
        <table>
            <tr>
              <td>1</td>
              <td>2</td>
            </tr>
            <tr>
              <td>3</td>
              <td>4</td>
            </tr>
        </table>
        """
        self.extractor = Extractor(html)
        self.extractor.parse()

    def test_return_list(self):
        self.assertEqual(
            self.extractor.return_list(),
            [[u'1', u'2'], [u'3', u'4']]
        )

class TestExtractorTransformer(unittest.TestCase):
    def setUp(self):
        html = """
        <table>
            <tr>
              <td>1</td>
              <td>2</td>
            </tr>
            <tr>
              <td>3</td>
              <td>4</td>
            </tr>
        </table>
        """
        self.extractor = Extractor(html, transformer=int)
        self.extractor.parse()

    def test_config_transformer(self):
        self.assertEqual(
            self.extractor.return_list(),
            [[1, 2], [3, 4]]
        )

class TestPassId(unittest.TestCase):
    def test_init_with_id(self):
        html = """
        <table id='wanted'>
            <tr>
              <td>1</td>
              <td>2</td>
            </tr>
            <tr>
              <td>3</td>
              <td>4</td>
            </tr>
        </table>
        <table id='unwanted'>
            <tr>
              <td>unwanted</td>
            </tr>
        </table>
        """
        soup = BeautifulSoup(html, 'html.parser')
        extractor = Extractor(soup, id_='wanted').parse()
        self.assertEqual(
            extractor.return_list(),
            [[u'1', u'2'], [u'3', u'4']]
        )

class TestComplexExtractor(unittest.TestCase):
    def setUp(self):
        html = """
        <table>
            <tr>
                <td rowspan=2>1</td>
                <td>2</td>
                <td>3</td>
            </tr>
            <tr>
                <td colspan=2>4</td>
            </tr>
            <tr>
                <td colspan=3>5</td>
            </tr>
        </table>
        """
        self.extractor = Extractor(html)
        self.extractor.parse()

    def test_return_list(self):
        self.assertEqual(
            self.extractor.return_list(),
            [[u'1', u'2', u'3'], [u'1', u'4', u'4'], [u'5', u'5', u'5']]
        )


class TestConflictedExtractor(unittest.TestCase):
    def setUp(self):
        html = """
        <table>
            <tr>
                <td rowspan=2>1</td>
                <td>2</td>
                <td rowspan=3>3</td>
            </tr>
            <tr>
                <td colspan=2>4</td>
            </tr>
            <tr>
                <td colspan=2>5</td>
            </tr>
        </table>
        """
        self.extractor = Extractor(html)
        self.extractor.parse()

    def test_return_list(self):
        self.assertEqual(
            self.extractor.return_list(),
            [[u'1', u'2', u'3'], [u'1', u'4', u'3'], [u'5', u'5', u'3']]
        )


if __name__ == '__main__':
    unittest.main()