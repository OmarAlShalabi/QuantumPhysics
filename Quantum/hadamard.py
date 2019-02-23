from projectq.ops import H, Measure,StatePreparation
from projectq import MainEngine
import projectq.setups.ibm
from projectq.backends import IBMBackend


#Intialization
ME = MainEngine(IBMBackend(), projectq.setups.ibm.get_engine_list())
rand_list = []


#random integer generation using 1 qubit and Hadamard gate
def getrandomquantum(mainengine):
    qubit = mainengine.allocate_qubit()
    H | qubit
    Measure | qubit
    rand_int = int(qubit)
    rand_list.append(rand_int)
    


for i in range(10):
   getrandomquantum(ME)


#Flush gates
ME.flush()
print(rand_list)
