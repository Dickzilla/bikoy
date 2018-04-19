'''
Created on 8 Apr 2018

@author: BIKOYPOGI
'''
# from controller.pmu import Pmu
from testprogram.pins.pinRef import PinRef
from testprogram.pins.pin import Pin
from testprogram.pins.pinGroup import PinGroup
from testprogram.tests.testRef import TestRef
from testprogram.tests.testType import TestType

class Test(TestRef):
    '''
    This is a generic PMU measurement instance.
    
    Attributes:
        name       String name for this test, eg. "Gpio18_PinCont" or "Vdd18_PsShorts"
        pinref     Pin reference where this applies to
        force      In Pmu, amount of current to force (in mA)
        delay      Time delay before acquiring measurement (in ms)
        meas       In Pmu, list of measured voltage (in V)
    '''


    def __init__(self, name: str, pinref: PinRef, testtype: TestType):
        '''
        Constructor
        '''
        TestRef.__init__(self, name) 
        self.pinref = pinref
        self.testtype = testtype
        self.meas = []
        self.flatpins = []
        self.expand_pins(self.pinref)
        
    def expand_pins(self, pinref: PinRef):
        if isinstance(pinref, Pin):
            self.flatpins.append(pinref)
        elif isinstance(pinref, PinGroup):
            self.expand_pins(pinref)
            
    def set_params(self, **kwargs):
        if self.testtype == TestType.BASIC:
            self.force = kwargs.get("force", 0.0)
            self.delay = kwargs.get("delay", 0.0)
            self.lolim = kwargs.get("lolim", 0.0)
            self.hilim = kwargs.get("hilim", 0.0)
        elif self.testtype == TestType.SWEEP:
            self.start = kwargs.get("start", 0.0)
            self.stop = kwargs.get("stop", 0.0)
            self.delay = kwargs.get("delay", 0.0)
        else:
            print("Unknown test type...")
    
#     def execute(self) -> list[float]:
#         ifvm = Pmu(self)
#         self.meas = ifvm.get()
#         return self.meas
