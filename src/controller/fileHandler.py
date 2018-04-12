'''
Created on 9 Apr 2018

@author: BIKOYPOGI
'''
import os
from testprogram.tests.testFlow import TestFlow
from testprogram.tests.testRef import TestRef
from testprogram.pins.pin import Pin
from testprogram.pins.pinGroup import PinGroup
from testprogram.pins.pinType import PinType
from testprogram.pins.pinRef import PinRef

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
                
    def load(self) -> TestFlow:
        self.testflow = TestFlow()
        self.testflow.tests = self.parse(self.fullpath)
        return self.testflow
            
    def parse(self, fullpath):
        pinA = Pin("PinA", "AA11", PinType.IO, 0x0001)
        pinB = Pin("PinB", "BB22", PinType.IO, 0x0002)
        ioGroup = PinGroup("IoGroup", PinType.IO)
        ioGroup.group.append(pinA, pinB)
        testIo = TestRef("IoTest", ioGroup, 100.0, 2.0)
        result = TestFlow(os.path.basename(self.fullpath))
        result.tests.append(testIo)
        return result
        