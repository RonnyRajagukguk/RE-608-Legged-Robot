import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

def run_forward():

    L1 = 8
    L2 = 6
    L3 = 4

    t = np.linspace(0, 40, 1000)

    q1 = 0.8 * np.sin(0.3 * t)
    q2 = 0.6 * np.cos(0.5 * t)
    q3 = 0.4 * np.sin(0.7 * t)

    plt.style.use("dark_background")

    fig, ax = plt.subplots(figsize=(7,7))

    ax.set_xlim(-20,20)
    ax.set_ylim(-20,20)
    ax.set_aspect("equal")
    ax.grid(True)

    workspace = plt.Circle((0,0), L1+L2+L3, fill=False, linestyle="--", alpha=0.4)
    ax.add_patch(workspace)

    link1, = ax.plot([],[], 'o-', lw=4)
    link2, = ax.plot([],[], 'o-', lw=4)
    link3, = ax.plot([],[], 'o-', lw=4)

    trajectory, = ax.plot([],[], lw=2)

    x_path = []
    y_path = []

    info = ax.text(0,-18,"",ha="center")

    def update(i):

        t1 = q1[i]
        t2 = q2[i]
        t3 = q3[i]

        x1 = L1*np.cos(t1)
        y1 = L1*np.sin(t1)

        x2 = x1 + L2*np.cos(t1+t2)
        y2 = y1 + L2*np.sin(t1+t2)

        x3 = x2 + L3*np.cos(t1+t2+t3)
        y3 = y2 + L3*np.sin(t1+t2+t3)

        link1.set_data([0,x1],[0,y1])
        link2.set_data([x1,x2],[y1,y2])
        link3.set_data([x2,x3],[y2,y3])

        x_path.append(x3)
        y_path.append(y3)

        trajectory.set_data(x_path,y_path)

        info.set_text(f"Forward Kinematics\nX={x3:.2f}  Y={y3:.2f}")

        return link1,link2,link3,trajectory,info

    animation = FuncAnimation(fig, update, frames=len(t), interval=30)

    plt.title("3 DOF Robot Arm - Forward Kinematics")
    plt.xlabel("X")
    plt.ylabel("Y")

    plt.show()