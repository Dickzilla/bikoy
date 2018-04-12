'''
Created on 28 Mar 2018

@author: BIKOYPOGI
'''
from testprogram.pins.pinRef import PinRef
from testprogram.pins.pinType import PinType

class Pin(PinRef):
    '''
    This is an instance of a DUT pin.
    
    Attributes:
        name       String name of this DUT pin, typically from package pinout, eg. "TMS"
        pinout     Pinout assignment from the package, eg "AB23"
        chtype     Tester channel type, eg either "IO" or "PWR"
        channel    Tester channel assignment/mapping, eg "0x0000" to "0xFFFF"
    '''

    def __init__(self, name, pinout: str, chtype: PinType, channel: int):
        '''
        Constructor
        '''
        PinRef.__init__(self, name)   
        self.pinout = pinout
        self.chtype = chtype
        self.channel = channel
        