#!/usr/bin/env python3
import numpy as np
import rebound as rb
import matplotlib.pyplot as plt
import os.path as path

def partc():
    # set up the simulation
    sim = rb.Simulation()
    sim.units = ('yr', 'AU', 'Msun')


    # Central mass
    M = 1.0
    sim.add(m=M)

    # from part b
    r = 1.0
    G = sim.G

    # Add a particle on a circular velocity
    vcirc = np.sqrt(G * M / r)

    # Start with circular velocity
    plotsim(vcirc, "partc_pos.pdf", "partc_velocity.pdf")



def partd():
    # set up the simulation
    sim = rb.Simulation()
    sim.units = ('yr', 'AU', 'Msun')


    # Central mass
    M = 1.0
    sim.add(m=M)

    # from part b
    r = 1.0
    G = sim.G

    # Add a particle on a circular velocity
    vcirc = np.sqrt(G * M / r)

    # Start with half circular velocity
    plotsim(vcirc / 2, "partd_pos.pdf", "partd_velocity.pdf")

def partf():
    # set up the simulation
    sim = rb.Simulation()
    sim.units = ('yr', 'AU', 'Msun')


    # Central mass
    M = 1.0
    sim.add(m=M)

    # from part b
    r = 1.0
    G = sim.G

    # Add a particle on a circular velocity
    vcirc = np.sqrt(G * M / r)

    # Try v > vcirc up to ~ v_esc
    fcirc = np.linspace(1.1, 1.4, 4)


    for i, fcirc in enumerate(fcirc):
        plotsim(vcirc * fcirc, f"partf_pos_{i}.pdf", f"partf_velocity_{i}.pdf", 1)

def plotsim(v0, fname_pos, fname_v, tscale = 1):
    # Same as in first bit but with v = 1/2 v_circ
    # set up the simulation
    sim = rb.Simulation()
    sim.units = ('yr', 'AU', 'Msun')

    # Central mass
    M = 1.0
    sim.add(m=M)

    # from part b
    r = 1.0
    G = sim.G


    vcirc = np.sqrt(G * M / r)
    sim.add(x=0, y=r, z=0, vx=v0, vy=0, vz=0)

    # Timesteping information
    t_total = 2.0 * tscale #yr
    t_step  = 0.01 #yr

    # Number of steps
    # Add 1 to include first step
    nt = int(t_total / t_step) + 1

    # Set up arrays
    t_arr = np.linspace(0, t_total, nt)
    x     = np.zeros(nt)
    y     = np.zeros(nt)
    vx    = np.zeros(nt)
    vy    = np.zeros(nt)


    # Finally, we can run the simulation
    for i, time in enumerate(t_arr):
        sim.integrate(time)
        # Grab the 2d positions and velocities of the test particle
        x[i]  = sim.particles[1].x
        y[i]  = sim.particles[1].y
        vx[i] = sim.particles[1].vx
        vy[i] = sim.particles[1].vy


    # Position plot
    fig, ax = plt.subplots(figsize=(6,6))
    ax.axis("equal")
    ax.scatter(x,y)

    ax.set_xlabel("x [AU]")
    ax.set_ylabel("y [AU]")

    vcirc = np.sqrt(G * M / r)
    vf = v0 / vcirc
    ax.set_title(f"$v_0 = {vf:.2f}" + r" v_{circ}$")



    fig.savefig(path.join("plots", fname_pos))

    # Velocity plot
    fig, ax = plt.subplots(figsize=(6,6))
    ax.scatter(t_arr,vx, label="$v_x$")
    ax.scatter(t_arr,vy, label="$v_y$")

    ax.set_title(f"$v_0 = {vf:.2f}" + r" v_{circ}$")

    ax.set_xlabel("t [yr]")
    ax.set_ylabel("$v$ [AU / yr]")





    ax.legend()
    fig.tight_layout()

    fig.savefig(path.join("plots", fname_v))


def main():
    partc()
    partd()
    partf()

if __name__ == '__main__':
    main()
