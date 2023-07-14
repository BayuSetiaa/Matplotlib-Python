import numpy as np
import matplotlib.pyplot as plt

#Membuat data
def sinusGenerator(amplitudo,frekuensi,tAkhir ,theta):
  t = np.arange(0,tAkhir,0.1)
  y = amplitudo*np.sin(2 * frekuensi * t + np.deg2rad(theta))
  return t, y

t1,y1 = sinusGenerator(1,1,4,0)
t2,y2 = sinusGenerator(1,1,4,90)
t3,y3 = sinusGenerator(1,1,4,180)

#Membuat plot
dataPlot1 = plt.plot(t1,y1)
dataPlot2 = plt.plot(t2,y2)
dataPlot3 = plt.plot(t3,y3)

#Setting properties
# plt.setp(plot,properti='nilai') #template
#Ada banyak propertis lainya cari aja di dokumentasinya matplotlib
plt.setp(dataPlot1,color='r',linestyle='-.',linewidth=0.75 )
plt.setp(dataPlot2,color='b',linestyle = ':',linewidth=1)
plt.setp(dataPlot3,color='g',linestyle = '--')

#Menampilkan show
plt.show()


