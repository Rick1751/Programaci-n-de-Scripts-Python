import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt
def dSdt(t,S,B):
    
    '''
    Use fd seguido de C-TAB para generar la funcion con docstrings
    Define el sistema de ecuaciones diferenciales para el movimiento del proyectil
    con resistencia al aire
    Parametros:
    t (float): Tiempo
    S (list): Estado actual [x, vx, y, vy]
    B (float): Coeficiente de resistencia del aire. Varía desde 0.0 a 1.0
    Retorna:
    list: Derivadas [dx/dt, dvx/dt, dy/dt, dvy/dt]
    '''

x, vx, y, vy = S
return [vx,
-B*np.sqrt(vx**2+vy**2)*vx,
vy,
-1-B*np.sqrt(vx**2+vy**2)*vy]
B = 0
V = 1
t1 = 40*np.pi/180
t2 = 45*np.pi/180
t3 = 50*np.pi/180
sol1 = solve_ivp(dSdt, [0, 2],
y0=[0,V*np.cos(t1),0,V*np.sin(t1)],
t_eval=np.linspace(0,2,1000),
args=(B,)) # atol=1e-7, rtol=1e-4)
sol2 = solve_ivp(dSdt, [0, 2],
y0=[0,V*np.cos(t2),0,V*np.sin(t2)],
t_eval=np.linspace(0,2,1000),
args=(B,)) #atol=1e-7, rtol=1e-4)
sol3 = solve_ivp(dSdt, [0, 2],
3
y0=[0,V*np.cos(t3),0,V*np.sin(t3)],
t_eval=np.linspace(0,2,1000),
args=(B,)) #atol=1e-7, rtol=1e-4)
plt.plot(sol1.y[0],sol1.y[2], label=r’$\theta_0=40^{\circ}$’)
plt.plot(sol2.y[0],sol2.y[2], label=r’$\theta_0=45^{\circ}$’)
plt.plot(sol3.y[0],sol3.y[2], label=r’$\theta_0=50^{\circ}$’)
plt.ylim(bottom=0)
plt.legend()
plt.xlabel(’$x/g$’, fontsize=20)
plt.ylabel(’$y/g$’, fontsize=20)
plt.show()