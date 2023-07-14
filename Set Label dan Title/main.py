import numpy as np
import matplotlib.pyplot as plt

#Membuat data
def sinusGenerator(amplitudo,frekuensi,tAkhir ,theta):
  t = np.arange(0,tAkhir,0.1)
  y = amplitudo*np.sin(2 * frekuensi * t + np.deg2rad(theta))
  return t, y

amplitudo = 1
frekuensi = 1
theta = 0
tAkhir = 4

t,y = sinusGenerator(amplitudo,frekuensi,tAkhir,theta)

#Membuat plot
#kalau ingin lebih dalam belajar membuat rumus matematika pakai latex search aja di google

judul = 'Grafik Sinusoidal\n'
rumus = r'$ \mathcal{Y} =A.sin(2 \omega t + \theta) $' + '\n '
parameter1 = r'$ A =  $' + str(amplitudo ) + ' cm, '
parameter2 = r'$ \omega = $' + str(frekuensi) + r'$ \mathit{Hz}$' + ', '
parameter3 = r'$ \theta = $' +  str(theta) + r'$ ^{o} $'

plt.plot(t,y)

#Membuat judul pastikan dibawah plot
plt.title(judul + rumus + parameter1 + parameter2 + parameter3)

#Membuat label pastikan dibawah plot
plt.xlabel('Waktu(detik)') #Membuat label di garis x atau bawah
plt.ylabel('Magnituda(cm)') #Membuat label digaris y 


#Menampilkan plot
plt.show()
