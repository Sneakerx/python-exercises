"""Unit tests for the circle module."""

import unittest
import circle
from math import pi


class TestCircle(unittest.TestCase):

    def test_calculate_area(self):
        # Test mit Radius 0
        self.assertEqual(circle.calculate_area(0), 0)

        # Test mit positivem Radius
        self.assertAlmostEqual(circle.calculate_area(1), pi)
        self.assertAlmostEqual(circle.calculate_area(2.5), pi * 2.5**2)

        # Test mit sehr großem Radius
        self.assertAlmostEqual(circle.calculate_area(1e6), pi * (1e6) ** 2)

        # Test mit negativem Radius (sollte ValueError werfen)
        with self.assertRaises(ValueError):
            circle.calculate_area(-1)

        # Test mit ungültigem Typ (sollte ValueError werfen)
        with self.assertRaises(TypeError):
            circle.calculate_area("invalid")

        with self.assertRaises(TypeError):
            circle.calculate_area(None)

    def test_calculate_circumference(self):
        # Test mit Radius 0
        self.assertEqual(circle.calculate_circumference(0), 0)

        # Test mit positivem Radius
        self.assertAlmostEqual(circle.calculate_circumference(1), 2 * pi)
        self.assertAlmostEqual(circle.calculate_circumference(2.5), 2 * pi * 2.5)

        # Test mit sehr großem Radius
        self.assertAlmostEqual(circle.calculate_circumference(1e6), 2 * pi * 1e6)

        # Test mit negativem Radius (sollte ValueError werfen)
        with self.assertRaises(ValueError):
            circle.calculate_circumference(-1)

        # Test mit ungültigem Typ (sollte ValueError werfen)
        with self.assertRaises(TypeError):
            circle.calculate_circumference("invalid")
        with self.assertRaises(TypeError):
            circle.calculate_circumference(None)


if __name__ == "__main__":
    unittest.main()
