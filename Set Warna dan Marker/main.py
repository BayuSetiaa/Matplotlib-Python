import numpy as np
import matplotlib.pyplot as plt

#Membuat data(sin(2wt + theta))
def sinusGenerator(amplitudo,frekuensi,tAkhir ,theta):
  t = np.arange(0,tAkhir,0.1)
  y = amplitudo*np.sin(2 * frekuensi * t + np.deg2rad(theta))
  return t, y

#Membuat Plot
t1,y1 = sinusGenerator(1,1,4,0)
plt.plot(t1,y1)

t2,y2 = sinusGenerator(1,1,4,30)
plt.plot(t2,y2, 'r') #Ini cara menambahkan warna , 'r' -> artinya red/merah

t3,y3 = sinusGenerator(1,1,4,60)
plt.plot(t3,y3, 'b--')#Untuk membuat garisnya jadi putus2 dan berwarna biru

t4,y4 = sinusGenerator(1,1,4,90)
plt.plot(t4,y4, 'b-o') #Untuk membuat garisnya ada bulat2nya

#Untuk marker lainya yg lebih banyak atau set warna dan garisnya bisa bukak di google 


#Menampilkan plot
plt.show()


