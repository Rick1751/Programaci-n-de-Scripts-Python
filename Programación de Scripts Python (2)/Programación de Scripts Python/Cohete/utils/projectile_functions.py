import numpy as np

def dSdt(t, S, B):
    x, vx, y, vy = S
    v = np.sqrt(vx**2 + vy**2)
    return [vx, -B*v*vx, vy, -1 - B*v*vy]

