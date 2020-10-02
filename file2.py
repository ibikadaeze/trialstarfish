#import things
import numpy as np
import matplotlib.pyplot as plt
from astropy.io import ascii

#read in files
file='Results.csv'
data = ascii.read(file,format='csv')
file2='datalteff.csv'
data2 = ascii.read(file2,format='csv')

#Mass-Radius
logM = np.log10(data['Mass'])
logR = data['lg_R']

plt.figure()

#Model data:
plt.plot(logR,logM)
plt.scatter(logR,logM)

#Homology relation #1:
x = np.linspace(3,6,100)

slope = 18./40
offset = -3 #You can set this to whatever to move the line close to your model data.
y = slope*x+offset # This is just linear because we are ploting log-log

plt.plot(x,y,color='r')

plt.xlabel('Log(Radius)')
plt.ylabel('Log(Mass)')
#plt.xlim(-1,2)
#plt.ylim(-1,5)
plt.show()
