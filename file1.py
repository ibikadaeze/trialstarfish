#import things
import numpy as np
import matplotlib.pyplot as plt
from astropy.io import ascii

# read in files
file='Results.csv'
data = ascii.read(file,format='csv')
file2='datalteff.csv'
data2 = ascii.read(file2,format='csv')

#HR Diagram
logTeff = np.log10(data['Teff'])
logL = data['lg_L']

plt.figure()

#Model data:
plt.plot(logTeff,logL, label = 'original model')
plt.scatter(logTeff,logL)

#Homology relation #1:
x = np.linspace(3,6,100)

slope = 284/69 #71/12. # This should be the exponent of the homology relationship
offset1 = -15.5 #You can set this to whatever to move the line close to your model data.
y1 = slope*x+offset1 # This is just linear because we are ploting log-log

#plt.plot(x,y,color='r')

slope = 60/7. #15 # This should be the exponent of the homology relationship
offset2 = -34 #You can set this to whatever to move the line close to your model data.
y2 = slope*x+offset2 # This is just linear because we are ploting log-log

slope = 80. # This should be the exponent of the homology relationship
offset3 = -150 #You can set this to whatever to move the line close to your model data.
y3 = slope*x+offset3 # This is just linear because we are ploting log-log

plt.plot(x,y1,'r',label='LMS')
         
plt.plot(x,y2,'k',label = 'HMS-gas')
plt.plot(x,y3,'m',label ='HMS-rad')

plt.xlabel('Log(Teff)')
plt.ylabel('Log(L/Lsun)')
plt.legend()
plt.xlim(5.0,3.0)
plt.ylim(-10,10)
#plt.show()
plt.savefig('ques3a.pdf')
