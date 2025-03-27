import function
import unittest   # The test framework

class Test_Functions(unittest.TestCase):
    def test_sum(self):
        self.assertEqual(function.sum(3,3), 6)


    def test_linear_search(self):
        result = function.linear_search([1,2,3,4,5], 3)

        self.assertEqual(result, 2)


    def test_linear_search_not_found_number(self):
        result = function.linear_search([1,2,3,4,5], 10)

        self.assertEqual(result, -10)

if __name__ == '__main__':
    unittest.main()