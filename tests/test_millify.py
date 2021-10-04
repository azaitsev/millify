import unittest
from millify import millify
from millify import prettify


class TestMillify(unittest.TestCase):
    """ Tests the millify() function. """

    def test_basics(self):
        self.assertEqual(millify(123), '123')
        self.assertEqual(millify(1234), '1k')
        self.assertEqual(millify(12345), '12k')
        self.assertEqual(millify(12345678), '12M')
        self.assertEqual(millify(1000000000), '1B')

    def test_precision(self):
        self.assertEqual(millify(1234, precision=2), '1.23k')
        self.assertEqual(millify(12345, precision=3), '12.345k')
        self.assertEqual(millify(12342123, precision=2), '12.34M')
        self.assertEqual(millify(12345123, precision=2), '12.35M')
        self.assertEqual(millify(12345678, precision=3), '12.346M')
        self.assertEqual(millify(12345678, precision=4), '12.3457M')

    def test_strings(self):
        self.assertEqual(millify('1234'), '1k')
        self.assertEqual(millify('12345'), '12k')
        self.assertEqual(millify('12345678'), '12M')

    def test_drop_nulls(self):
        self.assertEqual(millify(10000, precision=1, drop_nulls=False), '10.0k')
        self.assertEqual(millify(10000, precision=1, drop_nulls=True), '10k')
        self.assertEqual(millify(10000, precision=1), '10k')

    def test_prefixes(self):
        prefixes = ['kB', 'MB', 'GB']
        self.assertEqual(millify(10000, prefixes=None), '10k')
        self.assertEqual(millify(10000, prefixes=True), '10k')
        self.assertEqual(millify(10000, prefixes=prefixes), '10kB')
        self.assertEqual(millify(1000000, prefixes=prefixes), '1MB')
        self.assertEqual(millify(1000000000, prefixes=prefixes), '1GB')

    def test_nines(self):
        self.assertEqual(millify(999), '999')
        self.assertEqual(millify('999'), '999')
        self.assertEqual(millify(9999), '10k')
        self.assertEqual(millify(9999, precision=2), '10k')
        self.assertEqual(millify(99999), '100k')
        self.assertEqual(millify(999999), '1M')
        self.assertEqual(millify(999999999), '1B')


class TestPrettify(unittest.TestCase):
    """ Tests the prettify() function. """

    def test_basics(self):
        self.assertEqual(prettify(1234), '1,234')
        self.assertEqual(prettify(12345), '12,345')
        self.assertEqual(prettify(123456), '123,456')
        self.assertEqual(prettify(1234567), '1,234,567')
        self.assertEqual(prettify(1234567890), '1,234,567,890')

    def test_strings(self):
        self.assertEqual(prettify('1234'), '1,234')
        self.assertEqual(prettify('12345'), '12,345')
        self.assertEqual(prettify('123456'), '123,456')
        self.assertEqual(prettify('1234567'), '1,234,567')
        self.assertEqual(prettify('1234567890'), '1,234,567,890')

    def test_custom_separator(self):
        self.assertEqual(prettify('1234', separator=','), '1,234')
        self.assertEqual(prettify('12345', separator='.'), '12.345')
        self.assertEqual(prettify('123456', separator='/'), '123/456')
        self.assertEqual(prettify('1234567', separator='-'), '1-234-567')
        self.assertEqual(prettify('1234567890', separator=' '), '1 234 567 890')

    def test_separator_type(self):
        self.assertEqual(prettify('1234567890', separator=None), '1,234,567,890')
        self.assertEqual(prettify('1234567890', separator=True), '1,234,567,890')


if __name__ == '__main__':
    unittest.main()
