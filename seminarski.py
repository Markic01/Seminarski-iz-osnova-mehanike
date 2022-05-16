import matplotlib.pyplot as plt
import numpy as np

g=9.81

f=open('baseballforce.d')
lines=f.readlines()
f.close()

time=[float(x.split()[0]) for x in lines]
force=[float(x.split()[1]) for x in lines]

dt=time[1]-time[0]

ball_mass=0.145 #kg

#ugao ispaljivanja koliko god
angle=np.deg2rad(30)

#niz ubrzanja
Ax=[0]
Ay=[0]
#niz brzine
Vx=[0]
Vy=[0]
#niz vremena
Dt=[0]
#niz polozaja
Y=[0]
X=[0]

i=0

while Y[-1]>=0:

    if i>=len(force):
        Ax.append(0)
        Ay.append(-g)
    else:
        a=force[i]/ball_mass
        Ax.append(a*np.cos(angle))
        Ay.append(a*np.sin(angle)-g)

    Vx.append(Vx[-1]+Ax[-1]*dt)
    Vy.append(Vy[-1]+Ay[-1]*dt)

    X.append(X[-1]+Vx[-1]*dt)
    Y.append(Y[-1]+Vy[-1]*dt)

    Dt.append(Dt[-1]+dt)

    if i==len(force):
        print("Brzina loptice u trenutku kada napusti palicu:")
        print('Vx =',Vx[-1],'Vy = ',Vy[-1])
        print('|V| =',np.sqrt(Vx[-1]**2+Vy[-1]**2))
    
    i+=1

Ax=np.array(Ax)
Ay=np.array(Ay)
Vx=np.array(Vx)
Vy=np.array(Vy)
Dt=np.array(Dt)

A=(Ax**2+Ay**2)**(1/2)
V=(Vx**2+Vy**2)**(1/2)


plt.figure(1)
plt.title('Ubrzanje kroz celokupno vreme')
plt.xlabel('Vreme [s]')
plt.ylabel('Ubrzanje [m/s^2]')
plt.plot(Dt,A)
plt.show()

plt.figure(2)
plt.title('Ubrzanje u toku udaranja loptice')
plt.xlabel('Vreme [s]')
plt.ylabel('Ubrzanje [m/s^2]')
plt.plot(Dt[:len(force)],A[:len(force)])
plt.show()

plt.figure(3)
plt.title('Brzina kroz celokupno vreme')
plt.xlabel('Vreme [s]')
plt.ylabel('Brzina [m/s]')
plt.plot(Dt,V)
plt.show()

plt.figure(4)
plt.title('Brzina u toku udaranja loptice')
plt.xlabel('Vreme [s]')
plt.ylabel('Brzina [m/s]')
plt.plot(Dt[:len(force)],V[:len(force)])
plt.show()

plt.figure(5)
plt.title('Putanja')
plt.xlabel('X [m]')
plt.ylabel('Y [m]')
plt.plot(X,Y)
plt.show()
