from configobj import ConfigObj
import test_baseclass
import unittest


class TestAppConfig(test_baseclass.BaseTestCase):   
   def setUp(self):
      super(TestAppConfig, self).setUp()
      self.appConfig = ConfigObj(self.config['baseAppPath'] + '/apptype1/appname1/default/svdserch.conf')

   def test_is_visible_exists(self):      
      self.is_visible_value= self.appConfig['apple mac book os']['test.value1']
      self.assertEqual(self.is_visible_value, '-31@d')

  
if __name__ == '__main__':
    unittest.main()




