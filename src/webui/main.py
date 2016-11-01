'''

@author: zhang
'''

import unittest
import login,class2

# def setUpModule():  
#     print("setUpModule")  
#    
# def tearDownModule():  
#     print("tearDownModule")  

def suit():
    login_suit = login.suite()
    class2_suit = class2.suite()
    
    tss = unittest.TestSuite((login_suit,class2_suit))
    
    runner = unittest.TextTestRunner()
    runner.run(tss)
    
if __name__ == '__main__':
    suit()
