'''
Created on 8 Apr 2018

@author: BIKOYPOGI
'''

class ChType:
    '''
    This is a tester channel basic type enumeration.
    
    Attributes:
        IO         Used for I/O type tester pins, -400uA <= current <= +400uA
        PWR        Used for Power Supply type tester pins, -100mA <= current <= +100mA
    '''
    IO = 1
    PWR = 2
        