import unittest
import addTwoNumber


class TestSum(unittest.TestCase):
    def testCase1(self):
        self.assertEqual(addTwoNumber.addTwoNumbers(12,13), 25, "Should be 25")


def main():
    unittest.main()

    
if __name__ == "__main__":
    main()
    