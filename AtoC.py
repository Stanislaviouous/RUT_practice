import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.animation import PillowWriter

params={
    "qA1": 10000, 
    "qA2": 12000, 

    "qB1": 7000, 
    "qB2": 8000, 

    "c1": 13006.22, 
    "c2": 12485.97, 
    "T_AB": 9, 

    "kA1": 1408, 
    "kA2": 1874, 

    "kB1": 353, 
    "kB2": 58, 
    "d1": 209000, 
    "d2": 143000, 
    "P_AB": 250
    
    }

X_A1 = params["kA1"]
X_A2 = params["kA2"]

X_gran = min(X_A1, params["kB1"])
Y_gran = min(X_A2, params["kB2"])
P_gran = params["P_AB"]

S1 = params["d1"] - params["c1"] - params["qB1"] - params["qA1"]
S2 = params["d2"] - params["c2"] - params["qB2"] - params["qA2"]

print(S1, S2)

fig, ax = plt.subplots()

X_max = max(X_A1, params["kB1"])
Y_max = max(X_A2, params["kB2"])

x = np.arange(0, X_max + 50, 10)
y = np.arange(0, Y_gran + 50, 10)

lineX, = ax.plot(X_gran + 0 * y, y, label = f'x <= {X_gran}')
lineY, = ax.plot(x, Y_gran + 0 * x, label = f'y <= {Y_gran}')
lineP, = ax.plot(x, P_gran - x, label = f'x + y = {P_gran}')

lineS, = ax.plot(x,  (S1/S2) * x - (S1/S2) * x, label=f'{S1}x + {S2}y = T')
def animate(i):
    lineS.set_ydata(1 - (S1/S2) * x + i)
    print(i)
    if (i > 400):
        ani.event_source.stop()
    return lineS,

ani = animation.FuncAnimation(fig, animate, interval=1, blit=True, save_count=400)

ax.set_ylim(bottom=0.)
ax.set_xlim(left=0.)

plt.legend()
plt.show()

# Writer = PillowWriter(fps=30)
# ani.save('animationAtoС .gif', writer=Writer)

