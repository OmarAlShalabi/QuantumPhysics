import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np 



#Wavefunction
def wavefunc(r):
    a0 = .0529 

    return (27 - 18 * r / a0 + 2 * np.square(r) / np.square(a0)) * np.exp(-r / (3 * a0)) / (81 * np.sqrt(3 * np.pi) * (a0 ** (3/2)))


def testfunc(r):
    return 2 * np.exp(-0.5 * np.square(r/2)) * np.sin(2 * np.pi * r)

#Probability of the wavefunction
def Prob(x,y,z):
    rad = np.sqrt(np.square(x) + np.square(y) + np.square(z))
    return np.square(wavefunc(rad))


#Coordinates
x = np.linspace(-1,1,30)
y = np.linspace(-1,1,30)
z = np.linspace(-1,1,30)

elements = []
probs = []

for xe in x:
    for ye in y:
        for ze in z:
            elements.append(str((xe,ye,ze)))
            probs.append(Prob(xe,ye,ze))


probs = probs / sum(probs)


#Coordinates
cord = np.random.choice(elements,size = 35000, replace = True, p = probs)
cordmatrix = [i.split(',') for i in cord]
cordmatrix = np.matrix(cordmatrix)
x_coords = [float(i.item()[1:]) for i in cordmatrix[:,0]] 
y_coords = [float(i.item()) for i in cordmatrix[:,1]] 
z_coords = [float(i.item()[0:-1]) for i in cordmatrix[:,2]]


#Plot
fig = plt.figure(figsize = (10,10))
ax = Axes3D(fig)
ax.scatter(x_coords,y_coords,z_coords,alpha = 0.4 ,s = 2)
ax.set_title("Hydrogen (3,0,0) Probabilities")
plt.show()
