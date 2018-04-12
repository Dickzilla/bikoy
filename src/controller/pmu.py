'''
Created on 8 Apr 2018

@author: BIKOYPOGI
'''
from testprogram.tests import testRef
from time import sleep
from testprogram.pins.pinRef import PinRef
from testprogram.pins.pin import Pin
from testprogram.pins.pinGroup import PinGroup

class Pmu:
    '''
    Tester currently supports Pmu IFVM mode only.
    
    Attributes:
        testref    The name of the TestRef that needs the measurement
        result     Result of this Pmu measurement (in V)
    '''

    def __init__(self, testref: testRef.TestRef):
        '''
        Constructor
        '''
        self.testref = testref
        self.meas = []
        
    def get(self) -> list[float]:
        sleep(self.testref.delay/1000)
        pinref = self.testref.pinref
        self.getMeas(pinref)
        return self.meas
    
    def getMeas(self, pinref: PinRef):
        if type(pinref) == type(Pin):
            self.meas.append(0.75)
        elif type(self.testref.pinref) == type(PinGroup):
            group = PinGroup(self.testref.pinref)
            for pr in group:
                self.getMeas(pr)
        