import unittest
import xmlrunner
import test_baseclass
from configobj import ConfigObj

class TestSettingConfig(test_baseclass.BaseTestCase):   
   def setUp(self):
      super(TestSettingConfig, self).setUp()
      self.settingConfig = ConfigObj(self.config['baseAppPath'] + '/apptype1/appname1/metadata/setting.conf')

   def test_is_visible_exists(self):      
      self.is_visible_value= self.settingConfig['report']['is_visible']
      self.assertIsNotNone(self.is_visible_value)

   def test_auth_required_exists(self):      
      self.auth_required_value= self.settingConfig['report']['auth_required']
      self.assertIsNotNone(self.auth_required_value)

   def test_is_visible(self):      
      self.is_visible_value= self.settingConfig['report']['is_visible']
      self.assertEqual(self.is_visible_value, 'true')
      
   def test_auth_required(self):
      self.auth_required_value= self.settingConfig['report']['auth_required']
      self.assertEqual(self.auth_required_value, 'false')
      

if __name__ == '__main__':
    unittest.main(
        testRunner=xmlrunner.XMLTestRunner(output='test-reports'),
        # these make sure that some options that are not applicable
        # remain hidden from the help menu.
        failfast=False, buffer=False, catchbreak=False)




