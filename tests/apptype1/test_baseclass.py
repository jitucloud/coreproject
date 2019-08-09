import json
import unittest


class BaseTestCase(unittest.TestCase):
    def setUp(self):
        super(BaseTestCase, self).setUp()
        #.. set up that everyone needs ..
        with open('tests/apptype1/config.json','r') as f:
           self.config = json.load(f)

    def tearDown(self):
        #.. tear down that everyone needs ..
        super(BaseTestCase, self).tearDown()

    def test_common_test_cases(self):      
      self.assertEqual('true', 'true')
