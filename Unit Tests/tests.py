import surfshop
import unittest

class surfshoptest(unittest.TestCase):
  
  def setUp(self):
    self.ShoppingCart = surfshop.ShoppingCart()
    
  def test_add_surfboard_one(self):
    self.assertEqual(self.ShoppingCart.add_surfboards(1), 'Successfully added 1 surfboard to cart!')
  
  def test_add_surfboards(self):
    for num in range(2,5):
      with self.subTest(num=num):
        self.assertEqual(self.ShoppingCart.add_surfboards(num), f'Successfully added {num} surfboards to cart!')
        self.ShoppingCart = surfshop.ShoppingCart()
    
  
  def test_add_surfboard_five(self):
    self.assertRaises(surfshop.TooManyBoardsError,self.ShoppingCart.add_surfboards(5))


  def test_apply_locals_discount(self):
    self.ShoppingCart.apply_locals_discount()
    self.assertTrue(self.ShoppingCart.locals_discount)

  
unittest.main()
