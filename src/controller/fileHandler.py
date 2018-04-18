'''
Created on 9 Apr 2018

@author: BIKOYPOGI
'''
import os
from repo import *
from resources import *
from testprogram.pins import *
from testprogram.tests import *


class FileHandler:
    '''
    This class handles all file processing.
    
    Attributes:
        filepath   Directory and filename in dirPath/fileName.ext format
    '''


    def __init__(self, fullpath = None):
        '''
        Constructor
        '''
        if (fullpath != None):
            self.fullpath = fullpath
                
    def load(self) -> testFlow.TestFlow:
        self.testflow = self.parse(self.fullpath)
        return self.testflow
            
    def parse(self, fullpath: str):
        pinA = Pin("PinA", "AA11", PinType.IO, 0x0001)
        pinB = Pin("PinB", "BB22", PinType.IO, 0x0002)
        ioGroup = PinGroup("IoGroup", PinType.IO)
        ioGroup.group.append(pinA, pinB)
        testIo = TestRef("IoTest", ioGroup, 100.0, 2.0)
        result = TestFlow(os.path.basename(self.fullpath))
        result.tests.append(testIo)
        return result
        