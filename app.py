
import math
import numpy as np
import matplotlib.pyplot as plt
pi = math.pi
import streamlit as st

# maximum acceleration

m = st.slider('Mass (kg)', 0.0,100.0,40.0)
k = st.slider('Stiffness (kN/m)', 0.0,5000.0,800.)*1000
c = st.slider('Damping Coefficient (kN/(m/s))', 0.0,100.0,50.0)*1000
f = st.slider('Sin Forcing Frequency (Hz)', 0,1000,50)
accel = st.slider('Base Acceleration (g)',0,50,5)
#m = m  # Mass (kg)
#k = 800e3  # Spring constant (N/m)
#c = 1e3 #10e3  # Damping coefficient (N/(m/s))
#f = 22 #Hz
omega = 2*pi*f
a = accel*9.81/omega**2

t_max = 50/omega  # Maximum simulation time (s)
num_points = 10000
t = np.linspace(0, t_max, num_points)

zeta = c/(2*(k*m)**0.5)
p = (k/m)**0.5
X = a*(1 + (2*zeta*omega/p)**2)**0.5/((1 - (omega/p)**2)**2 + (2*zeta*omega/p)**2)**0.5
aMax = X*omega**2

print('zeta',zeta,'omega',omega,'p',p,X,aMax/9.81)
Fn = (k/m)**0.5/2/pi

st.text('Natural Frequency (Hz) = ' + str(round(Fn,2)))
st.text('Damping Ratio (zeta) = ' + str(round(zeta,2)))

X_a = (1 + (2*zeta*omega/p)**2)**0.5/((1 - (omega/p)**2)**2 + (2*zeta*omega/p)**2)**0.5
phi = np.arctan(2*zeta*(omega/p)**3/(1 + (4*zeta**2 - 1)*(omega/p)**2))

print('Fn',(k/m)**0.5/2/pi)
print(X_a,omega/p,phi)

y = a*np.sin(t*omega)
x = X_a*a*np.sin(omega*t - phi)
print('max x',max(x))
"""
font = {'family' : 'sans-serif',
'weight' : 'normal',
'size'   : 13}
plt.rc('font', **font)
styles = ['k-','b--','r:','g-.','m-','c--']

fig1 = plt.figure(1,figsize=(8,6))
#plt.title('TITLE')
plt.plot(t,y*1000,'-',linewidth = 3,label='Base Excitation')
plt.plot(t,x*1000,'--',linewidth = 3,label='Response')

plt.ylabel('Displacement (mm)')
#plt.ylim([0,100])
#plt.yticks()
plt.xlabel('Time (s)')
#plt.xlim([0,100])
#plt.xticks()

plt.grid()
plt.legend(loc='best')
st.pyplot(fig1)

fig2 = plt.figure(2,figsize=(8,6))
#plt.title('TITLE')
plt.plot(t,y*omega**2/9.81,'-',linewidth = 3,label='Base Excitation')
plt.plot(t,x*omega**2/9.81,'--',linewidth = 3,label='Response')

plt.ylabel('Acceleration (g)')
#plt.ylim([0,100])
#plt.yticks()
plt.xlabel('Time (s)')
#plt.xlim([0,100])
#plt.xticks()

plt.grid()
plt.legend(loc='best')

st.pyplot(fig2)
"""
