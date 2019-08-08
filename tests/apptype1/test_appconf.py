import unittest
import xmlrunner
from configobj import ConfigObj

class TestStringMethods(unittest.TestCase):    
   def setUp(self):
      self.config = ConfigObj('src/apptype1/appname1/default/app.conf')

   def test_is_visible_exists(self):      
      self.is_visible_value= self.config['report']['is_visible']
      self.assertIsNotNone(self.is_visible_value)

   def test_auth_required_exists(self):      
      self.auth_required_value= self.config['report']['auth_required']
      self.assertIsNotNone(self.auth_required_value)

   def test_is_visible(self):      
      self.is_visible_value= self.config['report']['is_visible']
      self.assertEqual(self.is_visible_value, 'true')
      
   def test_auth_required(self):
      self.auth_required_value= self.config['report']['auth_required']
      self.assertEqual(self.auth_required_value, 'false')
      

if __name__ == '__main__':
    unittest.main(
        testRunner=xmlrunner.XMLTestRunner(output='test-reports'),
        # these make sure that some options that are not applicable
        # remain hidden from the help menu.
        failfast=False, buffer=False, catchbreak=False)




