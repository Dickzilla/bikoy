'''
Created on 8 Apr 2018

@author: BIKOYPOGI
'''
from testprogram.pins.pinRef import PinRef
from testprogram.pins.pinType import PinType

class PinGroup(PinRef):
    '''
    This is an instance of a DUT pin group.
    
    Attributes:
        name       String name of this DUT pin group, eg. "GpioPins"
        chtype     Tester channel type for this group, eg "io" or "pwr"
        group      List of testprogram.Pin that belongs to this group, eg ['TMS', 'TDI']
    '''

    def __init__(self, name, chtype: PinType):
        '''
        Constructor
        '''
        PinRef.__init__(self, name)   
        self.chtype = chtype
        self.group = []
        