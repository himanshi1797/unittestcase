import unittest
import test


class TestCalc(unittest.TestCase):

    def test_isBase64(self):
        self.assertTrue(test.isBase64('aGVsbG8gd29ybGQ='))

    def test_decode_records(self):
        a = {1: 'aGVsbG8gd29ybGQ=', 2: 'aGVsbG8gd29ybGQ='}
        self.assertEqual(test.decode_records(a), {1: 'hello world', 2: 'hello world'})

    def test_generate_uuid(self):
        self.assertIsNotNone(test.generate_uuid())


    def test_get_current_timestamp(self):
        self.assertIsNotNone(test.get_current_timestamp())




if __name__ == '__main__' :
    unittest.main()