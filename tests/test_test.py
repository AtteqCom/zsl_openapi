from unittest import TestCase


class MyTestCase(TestCase):
    def test_it(self):
        self.assertEquals(True, True, "Error")
