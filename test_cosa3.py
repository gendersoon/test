import unittest
from cosa3 import birthdayCakeCandles

class TestCake(unittest.TestCase):

    def testCandles(self):
        self.assertEqual(birthdayCakeCandles(5, [2, 2, 2, 2, 2]), 5)
        def testHora(self):
            # Primer camino
            self.assertEqual(timeConversion("12:50:42AM"), "00:50:42")

            # Segundo camino
            self.assertEqual(timeConversion("05:12:56AM"), "05:12:56")

            # Tercer camino
            self.assertEqual(timeConversion("12:45:23PM"), "12:45:23")

            # Cuarto camino
            self.assertEqual(timeConversion("11:04:41PM"), "23:04:41")


if __name__ == '__main__':
    unittest.main()
