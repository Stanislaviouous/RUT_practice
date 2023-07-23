import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.animation import PillowWriter

params={
    "qA1": 10000, 
    "qA2": 12000, 

    "qB1": 9000, 
    "qB2": 3800, 

    "c1": 13375.89, 
    "c2": 12573.34, 
    "T_AB": 9, 

    "kA1": 1408, 
    "kA2": 1874, 

    "kB1": 243, 
    "kB2": 125, 
    "d1": 325000, 
    "d2": 263000, 
    "P_AB": 140
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
    if (i > 170):
        ani.event_source.stop()
    return lineS,

ani = animation.FuncAnimation(fig, animate, interval=1, blit=True, save_count=170)

ax.set_ylim(bottom=0.)
ax.set_xlim(left=0.)

plt.legend()
plt.show()

# Writer = PillowWriter(fps=30)
# ani.save('animationAtoE .gif', writer=Writer)

