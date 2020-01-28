from solution import node, solve_lca
import unittest
from unittest import mock
import io
import sys

class TestSolution(unittest.TestCase):
    """
    Test the solution for problem 1
    """

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def assert_stdout(self, nodes_map, input_val1, input_val2, expected_output, mock_stdout):
        solve_lca(nodes_map, input_val1, input_val2)
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    def setUp(self):
        nodes_map = dict()
        root_node = None
        for i in range(1, 10, 1):
            parent_node_value = i // 2
            parent_node = None
            if parent_node_value in nodes_map:
                parent_node = nodes_map[parent_node_value]

            current_node = node(i, parent_node)
            if parent_node == None:
                root_node = current_node
            nodes_map[i] = current_node
        return nodes_map

    def test_lca1(self):
        nodes_map = self.setUp()
        output = "3\n"
        self.assert_stdout(nodes_map, 6, 7, output)
    
    def test_lca2(self):
        nodes_map = self.setUp()
        output = "3\n"
        self.assert_stdout(nodes_map, 3, 7, output)

    def test_lca3(self):
        nodes_map = self.setUp()
        output = "1\n"
        self.assert_stdout(nodes_map, 8, 6, output)

if __name__ == '__main__':
    unittest.main()