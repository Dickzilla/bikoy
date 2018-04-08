'''
Created on 8 Apr 2018

@author: BIKOYPOGI
'''
from controller.ifvm import IFVM
from testprogram.pinref import PinRef
from testprogram.pin import Pin
from testprogram.pingroup import PinGroup

class TestRef:
    '''
    This is a generic PMU measurement instance.
    
    Attributes:
        name       String name for this test, eg. "Gpio18_PinCont" or "Vdd18_PsShorts"
        pinref     Pin reference where this applies to
        force      In IFVM, amount of current to force (in mA)
        delay      Time delay before acquiring measurement (in ms)
        meas       In IFVM, list of measured voltage (in V)
    '''


    def __init__(self, name: str, pinref: PinRef, force: float, delay: float):
        '''
        Constructor
        '''
        self.name = name
        self.pinref = pinref
        self.force = force
        self.delay = delay
        self.meas = []
    
    def get(self) -> list[float]:
        ifvm = IFVM(self)
        self.meas = ifvm.get()
        return self.meas