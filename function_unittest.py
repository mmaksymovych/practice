import function
import unittest   # The test framework

class BaseMathOperations(unittest.TestCase):
    def test_sum(self):
        result = function.sum(3,3)   

        self.assertEqual(result, 6)


    def test_multiply(self):
        result = function.multiply(3,3)   

        self.assertEqual(result, 9)


    def test_sumAndMultiplyAndSubstractResult(self):
        result = function.sumAndMultiplyAndSubstractResult(3,3)   

        self.assertEqual(result, 3)

    def test_linear_search_success(self):
        arr = [1,3,5,7,9,11,15]
        target = 7
        expected_index = 3

        result = function.linear_search(arr, target)

        self.assertEqual(result, expected_index)

    def test_linear_search_failed(self):
        arr = [1,3,5,7,9,11,15]
        target = 20
        expected_index = -1

        result = function.linear_search(arr, target)

        self.assertEqual(result, expected_index)
    


if __name__ == '__main__':
    unittest.main()