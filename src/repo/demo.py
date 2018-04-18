from lxml.etree import Element, SubElement, ElementTree

RavenRevA = Element('RavenRevA')
Gpio18_PinCont = SubElement(RavenRevA, 'Gpio18_PinCont')
Gpio18_Opens = SubElement(Gpio18_PinCont, 'Gpio18_Opens',
                          testtype='BASIC', 
                          pinref='Gpio18_Opens_Pins', 
                          force='100e-6',
                          lolim='200e-3', 
                          hilim='1.5', 
                          delay='2e-3')
Gpio18_Shorts = SubElement(Gpio18_PinCont, 'Gpio18_Opens', 
                           testtype='BASIC',
                           pinref='Gpio18_Opens_Pins', 
                           force='100e-6',
                           lolim='200e-3', 
                           hilim='1.5',
                           delay='2e-3')
Gpio18_Opens_Pins = SubElement(RavenRevA, 'Gpio18_Opens_Pins')
GpioPins = SubElement(Gpio18_Opens_Pins, 'GpioPins', 
                           PinType='IO',
                           Pin='PWROK')
JtagPins = SubElement(Gpio18_Opens_Pins, 'JtagPins', 
                           PinType='IO',
                           Pin='TCK')
Pins = SubElement(RavenRevA, 'Pins')
SubElement(Pins, 'PWROK', PinType='IO', Channel = '0x0000')
SubElement(Pins, 'RST_L', PinType='IO', Channel = '0x0001')
SubElement(Pins, 'TCK', PinType='IO', Channel = '0x0002')
SubElement(Pins, 'TMS', PinType='IO', Channel = '0x0003')

MainFlow = ElementTree(RavenRevA)
MainFlow.write('demo.xml', pretty_print=True)
        