import unittest
from probability import probability
from sympy import mpmath


class Probability(unittest.TestCase):
    """Test for probability.py"""

    def test_prob_1_sided_die(self):
        """ test for n = 1 : P(n=1) = 1
        """
        self.assertEqual(mpmath.nstr(probability(1), 8), "1.0")

    def test_prob_2_sided_die(self):
        """ test for n = 2 : P(n=1) = 0.5. This is like a coin toss.
            all outcomes = {HH, HT, TH, TT}
            desired outcomes = {HT, TH}
            probability = 2/4 = 0.5
        """
        self.assertEqual(mpmath.nstr(probability(2), 8), "0.5")

    def test_prob_wrong_input_zero(self):
        """
        If the input value n is zero, probability(n)
        would raise ValueError('Input not a positive integer')
        """
        with self.assertRaisesRegexp(ValueError, "positive"):
            mpmath.nstr(probability(0), 8)

    def test_prob_wrong_input_negative_number(self):
        """
        If the input value n is negative number, probability(n)
        would raise ValueError('Input not a positive integer')
        """
        with self.assertRaisesRegexp(ValueError, "positive"):
            mpmath.nstr(probability(-4), 8)

    def test_prob_wrong_input_string(self):
        """
        If the input value n is a string, probability(n)
        would raise ValueError('Input not of integer instance')
        """
        with self.assertRaisesRegexp(ValueError, "instance"):
            mpmath.nstr(probability("die"), 8)

    def test_prob_wrong_input_float(self):
        """
        If the input value n is float, probability(n)
        would raise ValueError('Input not of integer instance')
        """
        with self.assertRaisesRegexp(ValueError, "instance"):
            mpmath.nstr(probability(4.3), 8)

    def test_prob_wrong_input_negative_float(self):
        """
        If the input value n is negative float, probability(n)
        would raise ValueError('Input not of integer instance')
        """
        with self.assertRaisesRegexp(ValueError, "instance"):
            mpmath.nstr(probability(-4.3), 8)


if __name__ == "__main__":
    unittest.main()
