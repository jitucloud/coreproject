from configobj import ConfigObj
import test_baseclass
import unittest


class TestAppConfig(test_baseclass.BaseTestCase):   
   def setUp(self):
      super(TestAppConfig, self).setUp()
      self.appConfig = ConfigObj(self.config['baseAppPath'] + '/apptype1/appname1/default/app.conf')

   def test_is_visible_exists(self):      
      self.is_visible_value= self.appConfig['report']['is_visible']
      self.assertIsNotNone(self.is_visible_value)

   def test_auth_required_exists(self):      
      self.auth_required_value= self.appConfig['report']['auth_required']
      self.assertIsNotNone(self.auth_required_value)

   def test_is_visible(self):      
      self.is_visible_value= self.appConfig['report']['is_visible']
      self.assertEqual(self.is_visible_value, 'true')
      
   def test_auth_required(self):
      self.auth_required_value= self.appConfig['report']['auth_required']
      self.assertEqual(self.auth_required_value, 'false')
  
if __name__ == '__main__':
    unittest.main()




