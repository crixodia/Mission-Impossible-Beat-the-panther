import main
import unittest


class TestValidPassword(unittest.TestCase):
    def test_valid_passwords(self):
        message = "Is not a valid password"

        unittest.TestCase.assertTrue(not main.is_valid("password"), message)
        unittest.TestCase.assertTrue(not main.is_valid("12345678"), message)
        unittest.TestCase.assertTrue(not main.is_valid("Crix"), message)

        unittest.TestCase.assertTrue(main.is_valid("Crix1234"), message)
        unittest.TestCase.assertTrue(main.is_valid("Passw0rd"), message)


if __name__ == "__main__":
    unittest.main()
