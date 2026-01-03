import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt
import argparse
from utils.projectile_functions import dSdt

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-V', type=float, default=1.0)
    parser.add_argument('-B', type=float, default=0.0)
    parser.add_argument('-tmax', type=float, default=2.0)
    args = parser.parse_args()

    V = args.V
    B = args.B
    t_max = args.tmax
    
    t_eval = np.linspace(0, t_max, 1000)
    angulos = [40, 45, 50]
    
    for ang in angulos:
        rad = ang * np.pi / 180
        y0 = [0, V*np.cos(rad), 0, V*np.sin(rad)]
        sol = solve_ivp(dSdt, [0, t_max], y0=y0, t_eval=t_eval, args=(B,))
        plt.plot(sol.y[0], sol.y[2], label=f'$\\theta_0={ang}^\\circ$')

    plt.ylim(bottom=0)
    plt.legend()
    plt.xlabel('$x/g$', fontsize=20)
    plt.ylabel('$y/g$', fontsize=20)
    plt.show()

if __name__ == "__main__":
    main()
