#!/usr/bin/env python3
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

from scipy.integrate import solve_bvp, solve_ivp

def laneemden(xi, coords, n):
    t, u = coords
    # After make the substitution u = e^2 \frac{d\theta}{d\xi} the Lane-Emden equations become
    # \frac{du}{d\xi} = - \xi^2 \theta^n
    # \frac{d\theta}{d\xi} = u / \xi^2
    return (u / (xi + 0.00001)**2, -xi**2 * t**n)

def main():
    mpl.rc('font', size=18)

    xi = np.linspace(0,10, 1000)
    sol_n0   = solve_ivp(laneemden, [0, 10],y0=(1, 0),t_eval=xi, args=(0  , ))
    sol_n1   = solve_ivp(laneemden, [0, 10],y0=(1, 0),t_eval=xi, args=(1  , ))
    sol_n5   = solve_ivp(laneemden, [0, 10],y0=(1, 0),t_eval=xi, args=(5  , ))

    sol_n1d5 = solve_ivp(laneemden, [0, 10],y0=(1, 0),t_eval=xi, args=(1.5, ))
    sol_n3   = solve_ivp(laneemden, [0, 10],y0=(1, 0),t_eval=xi, args=(3  , ))

    fig, ax = plt.subplots(figsize=(9,6))

    ax.plot(sol_n0.t, sol_n0.y[0],label="$n_0=0$"   , linewidth=4)
    ax.plot(sol_n1.t, sol_n1.y[0], label="$n_0=1$"  , linewidth=4)
    ax.plot(sol_n1d5.t, sol_n1d5.y[0], label="$n_0=1.5$", linewidth=4)
    ax.plot(sol_n3.t, sol_n3.y[0], label="$n_0=3$"  , linewidth=4)
    ax.plot(sol_n5.t, sol_n5.y[0], label="$n_0=5$"  , linewidth=4)


    ax.plot(xi, 1 - (xi**2)/6, linestyle="dotted", color="black", linewidth=4, label="Analytic")
    ax.plot(xi, np.sin(xi)/xi, linestyle="dotted", color="black", linewidth=4)
    ax.plot(xi, 1/np.sqrt(1 + xi**2/3), linestyle="dotted", color="black", linewidth=4)

    ax.set_xlabel(r"$\xi$")
    ax.set_ylabel(r"$\theta$")

    ax.legend()

    ax.set_ylim(-1, 1.1)
    fig.tight_layout()
    fig.savefig("plots/problem4.png")



if __name__ == "__main__":
    main()
