import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

def run_inverse():

    L1 = 8
    L2 = 6
    L3 = 4

    targets = [(8,5),(10,2),(5,10),(-6,8),(-8,-2),(4,-6)]

    x_traj = []
    y_traj = []

    for i in range(len(targets)):

        x0,y0 = targets[i]
        x1,y1 = targets[(i+1)%len(targets)]

        t = np.linspace(0,1,80)

        x_traj.extend(x0 + (x1-x0)*t)
        y_traj.extend(y0 + (y1-y0)*t)

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

    path, = ax.plot([],[], lw=2)
    target_point, = ax.plot([],[], 'ro')

    x_hist=[]
    y_hist=[]

    info=ax.text(0,-18,"",ha="center")

    def update(i):

        x=x_traj[i]
        y=y_traj[i]

        phi = 0.3*np.sin(i*0.03)

        xw = x - L3*np.cos(phi)
        yw = y - L3*np.sin(phi)

        D = (xw**2 + yw**2 - L1**2 - L2**2)/(2*L1*L2)
        D = np.clip(D,-1,1)

        theta2 = np.arccos(D)

        theta1 = np.arctan2(yw,xw) - np.arctan2(L2*np.sin(theta2), L1 + L2*np.cos(theta2))

        theta3 = phi - theta1 - theta2

        x1=L1*np.cos(theta1)
        y1=L1*np.sin(theta1)

        x2=x1+L2*np.cos(theta1+theta2)
        y2=y1+L2*np.sin(theta1+theta2)

        x3=x2+L3*np.cos(theta1+theta2+theta3)
        y3=y2+L3*np.sin(theta1+theta2+theta3)

        link1.set_data([0,x1],[0,y1])
        link2.set_data([x1,x2],[y1,y2])
        link3.set_data([x2,x3],[y2,y3])

        x_hist.append(x3)
        y_hist.append(y3)

        path.set_data(x_hist,y_hist)

        target_point.set_data(x,y)

        info.set_text(f"Target: ({x:.2f},{y:.2f})\nEnd Effector: ({x3:.2f},{y3:.2f})")

        return link1,link2,link3,path,target_point,info

    animation = FuncAnimation(fig,update,frames=len(x_traj),interval=40)

    plt.title("3 DOF Robot Arm - Inverse Kinematics")
    plt.xlabel("X")
    plt.ylabel("Y")

    plt.show()