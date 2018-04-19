'''
Created on 9 Apr 2018

@author: BIKOYPOGI
'''
from testprogram.tests.testRef import TestRef
from testprogram.tests.test import Test

class TestFlow(TestRef):
    '''
    This is the main test program flow which contain the tests.
    
    Attributes:
        name       String name of this test program, eg. "RavenRevA"
        tests      List of tests that will be performed, eg ['Gpio18_PinCont', 'Vdd18_PsShorts']
    '''


    def __init__(self, name: str, testref: TestRef):
        '''
        Constructor
        '''
        TestRef.__init__(self, name) 
        self.testref = testref
        self.tests = []
        self.expand_tests(self.testref)
        
    def expand_tests(self, testref: TestRef):
        if isinstance(testref, Test):
            self.tests.append(testref)
        elif isinstance(testref, TestFlow):
            self.expand_tests(testref)
        