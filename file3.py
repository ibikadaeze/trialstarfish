#import things
import numpy as np
import matplotlib.pyplot as plt
from astropy.io import ascii

#read in files
file='Results.csv'
data = ascii.read(file,format='csv')
file2='datalteff.csv'
data2 = ascii.read(file2,format='csv')

#Mass-Lum
logM = np.log10(data['Mass'])
logL = data['lg_L']

plt.figure()

#Model data:
plt.plot(logM,logL)
plt.scatter(logM,logL)

#Homology relation #1:
x = np.linspace(3,6,100)

slope = 5# This shssh -X kalexand@login.aoc.nrao.edu ould be the exponent of the homology relationship
offset = -10 #You can set this to whatever to move the line close to your model data.
y = slope*x+offset # This is just linear because we are ploting log-log

plt.plot(x,y,color='r')

plt.ylabel('Log(Luminosity)')
plt.xlabel('Log(Mass)')
plt.xlim(-1,2.5)
plt.ylim(-2,8)
plt.show()
plt.savefig('yes.png')
