'''
Created on 19 Apr 2018

@author: BIKOYPOGI
'''
from testprogram.tests.testRef import TestRef
from testprogram.pins.pinRef import PinRef
from lxml import etree

class Tp:
    '''
    Holds the whole testprogram
    '''


    def __init__(self):
        '''
        Constructor
        '''
        self.testref = TestRef()
        self.pinref = PinRef()
        self.tree = etree.ElementTree()
        