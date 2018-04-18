'''
Created on 15 Apr 2018

@author: BIKOYPOGI
'''

class TestType(object):
    '''
    This is a PMU test basic type enumeration.
    
    Attributes:
        Basic      Point test. Params include force, loLim, hiLim and delay
        Sweep      Charz test. Params include start, stop, step and delay
    '''
    BASIC = 1
    SWEEP = 2