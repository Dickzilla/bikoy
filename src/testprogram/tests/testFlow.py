'''
Created on 9 Apr 2018

@author: BIKOYPOGI
'''
from ctypes.test.test_pickling import name

class TestFlow(object):
    '''
    This is the main test program flow which contain the tests.
    
    Attributes:
        name       String name of this test program, eg. "RavenRevA"
        tests      List of tests that will be performed, eg ['Gpio18_PinCont', 'Vdd18_PsShorts']
    '''


    def __init__(self, name: str):
        '''
        Constructor
        '''
        self.name = name
        self.tests = []
        