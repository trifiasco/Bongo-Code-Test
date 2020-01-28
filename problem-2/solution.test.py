from solution import print_depth, Person
import unittest
from unittest import mock
import io
import sys

class TestSolution(unittest.TestCase):
    """
    Test the solution for problem 1
    """

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def assert_stdout(self, input_val, expected_output, mock_stdout):
        print_depth(input_val)
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    def test_dictionary_with_object(self):
        person_a = Person("User", "1", None)
        person_b = Person("User", "2", person_a)

        a = {
            "key1": 1,
            "key2": {
                "key3": 1,
                "key4": {
                    "key5": 4,
                    "user": person_b
                }
            }
        }
        output = "key1 : 1\nkey2 : 1\nkey3 : 2\nkey4 : 2\nkey5 : 3\nuser : 3\nfather : 4\nfirst_name : 4\nlast_name : 4\nfather : 5\nfirst_name : 5\nlast_name : 5\n"
        self.assert_stdout(a, output)

if __name__ == '__main__':
    unittest.main()