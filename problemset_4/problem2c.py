#!/usr/bin/env python3
import numpy as np
from scipy.optimize import fsolve
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt
import matplotlib as mpl

def windeq(v, r, cs, rs):
    """Equation 1 from the homework, with all terms moved to 1 side"""
    x = rs / r
    return (
             + v
             * np.exp(
                      - v**2
                      / (
                         2
                         *cs**2
                        )
                     )
             - cs
             * x**2
             * np.exp(
                      + 3/2
                      - 2
                      * x
                     )
    )

def breezeeq(r, v, cs, GM):
    """Equation 2 from the homework with solved for dv/dr"""
    return (
            + v
            / (
               + v**2
               - cs**2
              )
            * (
                + 2
                * cs**2
                / r
                - GM
                / r**2
              )
    )


def plot_wind(ax):
    n = 100

    # Solve out to 3 times the scale radius
    rspace = np.linspace(0.01, 3, n)
    vspace = np.zeros(n)

    # initial guesses
    vguess = np.zeros(n)
    vguess[rspace > 1] = 2.0

    for n,(r, v0) in enumerate(zip(rspace, vguess)):
        vspace[n] = fsolve(windeq, v0, args=(r, 1, 1))[0]

    ax.plot(rspace, vspace, linewidth=3, label="Wind solution")

def plot_breeze(ax):
    n = 100
    cs, GM = 1, 2

    # Solve out to 3 times the scale radius
    t_span = (0.01,3)
    rspace = np.linspace(*t_span, n)
    sol = solve_ivp(windeq, t_span=t_span, y0=(0.01, ), t_eval=rspace, args=(cs, GM))

    ax.plot(sol.t, sol.y[0], linewidth=3, label="Breeze solution")


def main():
    mpl.rc('font', size=18)
    fig, ax = plt.subplots(figsize=(9,6))

    plot_wind(ax)
    plot_breeze(ax)

    ax.set_xlabel("$r / r_s$")
    ax.set_ylabel("$v / c_s$")

    ax.legend()

    fig.savefig("plots/windbreeze.png")


if __name__ == "__main__":
    main()
