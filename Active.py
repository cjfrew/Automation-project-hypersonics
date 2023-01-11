import pyvisa
import os
import time

rm = pyvisa.ResourceManager()

#Give list of all connected components 
print("Resources detected\n{}\n".format(rm.list_resources()))

supply = None #enter ID of supply (use Get_resource.py)
monitor = None #enter ID of multimeter 

#Set supply to known value 
supply.write(':OUTP CH1,OFF')   # start OFF - safe :)
supply.write(':APPL ch1, 0, 0:2')

