import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

def run_forward():

    # =========================
    # PARAMETER ROBOT (3 DOF)
    # =========================
    L1, L2, L3 = 8, 6, 4

    t = np.linspace(0, 40, 1200)

    # trajectory sudut (TETAP)
    theta1 = 0.8*np.sin(0.3*t)
    theta2 = 0.6*np.cos(0.5*t)
    theta3 = 0.4*np.sin(0.7*t)
    

    # =========================
    # SETUP VISUAL (IMPROVED)
    # =========================
    plt.style.use('dark_background')

    fig, ax = plt.subplots(figsize=(7,7))

    ax.set_xlim(-20,20)
    ax.set_ylim(-20,20)
    ax.set_aspect('equal')

    # grid halus
    ax.grid(True, linestyle='--', alpha=0.3)

    # workspace
    circle = plt.Circle((0,0), L1+L2+L3,
                        fill=False,
                        linestyle="--",
                        linewidth=1.5,
                        alpha=0.4)
    ax.add_patch(circle)

    # robot (dipisah biar beda warna)
    line1, = ax.plot([], [], 'o-', lw=5)
    line2, = ax.plot([], [], 'o-', lw=5)
    line3, = ax.plot([], [], 'o-', lw=5)

    traj, = ax.plot([], [], lw=2)

    text = ax.text(0, -18, '',
                   ha='center',
                   fontsize=10,
                   bbox=dict(facecolor='black',
                             alpha=0.6,
                             edgecolor='white'))

    x_hist, y_hist = [], []

    # =========================
    # UPDATE ANIMATION
    # =========================
    def update(i):

        t1 = theta1[i]
        t2 = theta2[i]
        t3 = theta3[i]

        # =========================
        # FORWARD KINEMATICS
        # =========================
        x1 = L1*np.cos(t1)
        y1 = L1*np.sin(t1)

        x2 = x1 + L2*np.cos(t1+t2)
        y2 = y1 + L2*np.sin(t1+t2)

        x3 = x2 + L3*np.cos(t1+t2+t3)
        y3 = y2 + L3*np.sin(t1+t2+t3)

        # =========================
        # DRAW ROBOT
        # =========================
        line1.set_data([0,x1],[0,y1])
        line1.set_color('cyan')

        line2.set_data([x1,x2],[y1,y2])
        line2.set_color('yellow')

        line3.set_data([x2,x3],[y2,y3])
        line3.set_color('magenta')

        # trajectory end-effector
        x_hist.append(x3)
        y_hist.append(y3)
        traj.set_data(x_hist, y_hist)
        traj.set_color('orange')

        # info text
        text.set_text(
            f"Forward Kinematics\n"
            f"X = {x3:.2f}, Y = {y3:.2f}"
        )

        return line1, line2, line3, traj, text

    # =========================
    # ANIMATION
    # =========================
    anim = FuncAnimation(
        fig,
        update,
        frames=len(t),
        interval=30
    )

    plt.title("3 DOF Robot - Forward Kinematics (Enhanced)",
              fontsize=13, weight='bold')

    plt.xlabel("X Position")
    plt.ylabel("Y Position")

    plt.show()


# RUN
run_forward()