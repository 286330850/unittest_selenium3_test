'''

@author: zhang
'''

import unittest

class Class2(unittest.TestCase):

    def setUp(self):
        print('tc setup')

    def test_class2_future1(self):
        print('test class2 future1')
    
    def test_class2_future2(self):
        print('test class2 future2')
    
    def tearDown(self):
        print('tc teardown')

    @classmethod  
    def setUpClass(cls):  
        print("class2 setUpClass")  
 
    @classmethod  
    def tearDownClass(cls):  
        print("class2 tearDownClass")  
        
def suite():
    return unittest.makeSuite(Class2, "test")        