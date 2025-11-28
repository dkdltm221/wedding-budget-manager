import unittest
from utils.params import parse_int, parse_pagination
from utils.formatting import format_currency
from services.guests_service import parse_amount


class TestUtils(unittest.TestCase):
    def test_parse_int_bounds(self):
        self.assertEqual(parse_int("10", 1, min_value=5, max_value=20), 10)
        self.assertEqual(parse_int("2", 1, min_value=5, max_value=20), 1)  # below min
        self.assertEqual(parse_int("30", 1, min_value=5, max_value=20), 1)  # above max
        self.assertEqual(parse_int("abc", 3), 3)

    def test_parse_pagination(self):
        args = {"page": "2", "per_page": "50"}
        page, per_page = parse_pagination(args, default_page=1, default_per_page=20, max_per_page=100)
        self.assertEqual(page, 2)
        self.assertEqual(per_page, 50)

        args = {"page": "-1", "per_page": "500"}
        page, per_page = parse_pagination(args, default_page=1, default_per_page=20, max_per_page=100)
        self.assertEqual(page, 1)        # reset to default
        self.assertEqual(per_page, 20)   # reset to default because above max

    def test_format_currency(self):
        self.assertEqual(format_currency(1234567), "1,234,567")

    def test_parse_amount(self):
        self.assertEqual(parse_amount("0"), 0)
        self.assertEqual(parse_amount("10"), 10)
        with self.assertRaises(ValueError):
            parse_amount("-1")
        with self.assertRaises(ValueError):
            parse_amount("abc")


if __name__ == '__main__':
    unittest.main()
