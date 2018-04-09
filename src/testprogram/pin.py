'''
Created on 28 Mar 2018

@author: BIKOYPOGI
'''
from testprogram.pinref import PinRef
from testprogram.chType import ChType

class Pin(PinRef):
    '''
    This is an instance of a DUT pin.
    
    Attributes:
        name       String name of this DUT pin, typically from package pinout, eg. "TMS"
        pinout     Pinout assignment from the package, eg "AB23"
        chtype     Tester channel type, eg either "IO" or "PWR"
        channel    Tester channel assignment/mapping, eg "0x00" to "0xFFF"
    '''

    def __init__(self, name, pinout: str, chtype: ChType, channel: int):
        '''
        Constructor
        '''
        PinRef.__init__(self, name)   
        self.pinout = pinout
        self.chtype = chtype
        self.channel = channel
        