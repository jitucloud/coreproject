import unittest
from configobj import ConfigObj

class AppConf(unittest.TestCase):    
    def setUp(self):      
        self.config = ConfigObj('../parent/apptype1/appname1/app.conf')

    def is_visible(self):
        self.is_visible_value= self.config['report']['is_visible']
        self.assertEqual(self.is_visible_value, 'true') 

    def auth_required(self):
        self.auth_required_value= self.config['report']['auth_required']
        self.assertEqual(self.auth_required_value, 'false') 

if __name__ == '__main__':
    unittest.main()




