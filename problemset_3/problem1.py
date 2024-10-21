#!/usr/bin/env python3
import numpy as np
import matplotlib  as mpl
import matplotlib.pyplot as plt

def plot_streamline(ax, C, ab, theta, kwargs_plot={}):
    r = C * np.exp(ab * theta)

    x = r * np.cos(theta)
    y = r * np.sin(theta)

    ax.plot(x,y, **kwargs_plot)

def main():
    mpl.rc('font', size=18)
    fig, ax = plt.subplots(figsize=(9,8))
    theta = np.linspace(0, 2 * np.pi, 1000)
    plot_streamline(ax,
                    C=1,
                    ab=1,
                    theta=theta,
                    kwargs_plot=dict(linewidth=3, label="C=1, a/b=1")
                   )
    plot_streamline(ax,
                    C=-1,
                    ab=1,
                    theta=theta,
                    kwargs_plot=dict(linewidth=3, label="C=-1, a/b=1")
                   )
    ax.set_xlabel("x / |C|")
    ax.set_ylabel("y / |C|")
    ax.legend()
    fig.savefig("plots/spiral.png")

if __name__ == "__main__":
    main()
