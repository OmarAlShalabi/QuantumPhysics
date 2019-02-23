from projectq.ops import H, Measure,StatePreparation
from projectq import MainEngine
import numpy as np
from qutip import Bloch

#Intialization
ME = MainEngine()


#Input
x,y = map(complex,input("enter the state: ").split())

#Normalization
norm = np.sqrt(np.abs(x**2) + np.abs(y**2))
x /= norm
y /= norm

#Qubit allocation , define a state for the qubit,and  measure it.
qubit = ME.allocate_qubit()
StatePreparation([x,y]) | qubit
Measure | qubit
read = int(qubit)


#Measuring output
ME.flush()
print(read)


#State vector to sphereical coordinates
phi = np.angle(y) - np.angle(x)
theta = 2 * np.arccos(np.abs(x))
vec = [np.sin(theta) * np.cos(phi), np.sin(theta) * np.sin(phi), np.cos(theta)]

#Visualization
b = Bloch()
b.add_vectors(vec)
b.show()
