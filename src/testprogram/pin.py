'''
Created on 28 Mar 2018

@author: BIKOYPOGI
'''

class Pin:
    '''
    This is an instance of a DUT pin.
    
    Attributes:
        name       String name of this DUT pin, typically from package pinout, eg. "TMS"
        channel    Tester channel assignment/mapping, eg "AB23"
    '''

    def __init__(self, name, channel):
        self.name = name
        self.channel = channel
        