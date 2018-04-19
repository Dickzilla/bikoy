from lxml.etree import Element, SubElement, ElementTree

# Tests and Flows
RavenRevA = Element('TestRef', name='RavenRevA')
Gpio18_PinCont = SubElement(RavenRevA, 'TestFlow', name='Gpio18_PinCont')
Gpio18_Opens = SubElement(Gpio18_PinCont, 'Test', name='Gpio18_Opens',
                          testtype='BASIC', 
                          pinref='Gpio18_Opens_Pins', 
                          force='100e-6',
                          lolim='200e-3', 
                          hilim='1.5', 
                          delay='2e-3')
Gpio18_Shorts = SubElement(Gpio18_PinCont, 'Test', name='Gpio18_Shorts', 
                           testtype='BASIC',
                           pinref='Gpio18_Opens_Pins', 
                           force='100e-6',
                           lolim='200e-3', 
                           hilim='1.5',
                           delay='2e-3')
MainFlow = ElementTree(RavenRevA)
MainFlow.write('tests.xml', pretty_print=True)


# Pins and Pingroups
RavenPins = Element('PinRef', name='RavenPins')
Gpio18_Opens_Pins = SubElement(RavenPins, 'PinGroup', name='Gpio18_Opens_Pins')

GpioPins = SubElement(Gpio18_Opens_Pins, 'PinGroup', name='GpioPins', PinType='IO')
SubElement(GpioPins, 'Pin', name='PWROK')
SubElement(GpioPins, 'Pin', name='RST_L')

JtagPins = SubElement(Gpio18_Opens_Pins, 'PinGroup', name='JtagPins', PinType='IO')
SubElement(JtagPins, 'Pin', name='TCK')
SubElement(JtagPins, 'Pin', name='TMS')

Pins = SubElement(RavenPins, 'Pins')
SubElement(Pins, 'PWROK', PinType='IO', Channel = '0x0000')
SubElement(Pins, 'RST_L', PinType='IO', Channel = '0x0001')
SubElement(Pins, 'TCK', PinType='IO', Channel = '0x0002')
SubElement(Pins, 'TMS', PinType='IO', Channel = '0x0003')

PinDef = ElementTree(RavenPins)
PinDef.write('pins.xml', pretty_print=True)

        