from matplotlib import gridspec
from textwrap import wrap
import matplotlib.pyplot as plt
import math

def drawPlots(plots, x, y, k):
    plt.switch_backend('Qt5Agg')
    fig = plt.gcf()
    fig.canvas.set_window_title('Rozkład słów sekwencji DNA')
    plotNum = len(plots)
    cols = 2
    rows = int(math.ceil(plotNum / cols))
    gs = gridspec.GridSpec(rows, cols)
    rxf = []

    for n in range(plotNum):
        ax = plt.subplot(gs[n])
        if (plots[n] == "zwykły"):
            ax.set_title("Rozkład zwykły")
            ax.set_xlabel("r")
            ax.set_ylabel("f", rotation=0, labelpad=15)

        if (plots[n] == "logarytmiczny"):
            ax.set_title("\n".join(wrap("Rozkład w skali logarytmicznej", 25)))
            ax.set_xscale("log")
            ax.set_yscale("log")
            ax.set_xlabel("r")
            ax.set_ylabel("f", rotation=0, labelpad=10)

        if (plots[n] == "rozkład Zipfa"):
            ax.set_title("\n".join(wrap("Rozkład Zipfa", 25)))
            ax.set_yscale("log")
            ax.set_xlabel("r")
            ax.set_ylabel("r x f", rotation=0, labelpad=15)
            for c, i in enumerate(x):
                rxf.append(i * y[c])
            ax.plot(x, rxf)

        if (plots[n] == "histogram"):
            ax.set_title("Histogram rozkładu")
            ax.set_xlabel("f")
            ax.set_ylabel("n(f)", rotation=0, labelpad=15)
            num_bins = len(x)
            ax.hist(y, bins=num_bins, facecolor='purple')


        if (plots[n] != "histogram" and plots[n] != "rozkład Zipfa"):
            ax.plot(x, y)

    plt.subplots_adjust(top=0.85, wspace=0.5, hspace=0.6)
    plt.suptitle("Długość słów k = " + str(k))
    # ax.legend(bbox_to_anchor=(1.05, 0), loc='bottom', borderaxespad=0.)
    plt.show()
