import product
import unittest
class testproduct(unittest.TestCase):
    def test_display_product_details(self):
        obj1 = product("iphone",20000,18000,4.0)
        self.assertEqual(obj1.display_product_details)

