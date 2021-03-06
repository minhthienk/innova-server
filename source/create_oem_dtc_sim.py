
from common.simulation import *


ymme_dict = {'name':'test', 'year':2003, 
                'make':'Ford', 
                'model':'Escape', 
                'engine':'L4, 2.0L',
                'system':None,
                'protocol': 'PROTOCOL_ISO9141'}

fordsim = FordSimulation(ymme_dict)
sim_data = fordsim.create_dtc()

print(sim_data)



