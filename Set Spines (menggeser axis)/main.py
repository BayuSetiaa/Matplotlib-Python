import numpy as np
import matplotlib.pyplot as plt

#Membuat data 
sudut = np.arange(0,360,1)
y = np.sin(np.deg2rad(sudut))

#buat plot
plt.plot(sudut, y)
plt.title('Grafik Sinusoidal')
plt.text(190,1,'Magnituda') #190,1 -> itu lokasinya
plt.text(360,0.1,'Sudut') 

plt.yticks([-1,-0.5,0,0.5,1]) 
plt.xticks([0,90,180,270,360],[r'${0}^o$', r'${90}^o$', r'${180}^o$', r'${270}^o$', r'${360}^o$'])

#Cara ambil axis atau geser axis
ax = plt.gca()
ax.spines['left'].set_position(('data',180))
ax.spines['bottom'].set_position(('data',0))
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')


#Tampilin plot
plt.show()