import unittest
from zoo import Zoo

class TestZoo(unittest.TestCase):
    def setUp(self):
        self.zoo = Zoo()

    def test_negative_ticket_price(self):
        self.assertEqual(self.zoo.get_ticket_price(-1), 0)

    def test_age_zero_to_twelve(self):
        self.assertEqual(self.zoo.get_ticket_price(12), 50)

    def test_age_thirteen_to_twenty(self):
        self.assertEqual(self.zoo.get_ticket_price(15), 100)

    def test_age_twenty_one_to_sixty(self):
        self.assertEqual(self.zoo.get_ticket_price(30), 150)

    def test_age_over_sixty(self):
        self.assertEqual(self.zoo.get_ticket_price(65), 100)

if __name__ == '__main__':
    unittest.main()
