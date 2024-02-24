from matplotlib import pyplot as plt
import numpy as np
import seaborn as sns

from backstrip import backstrip


def test_backstrip_v():
    plt.clf()
    # adapted from https://matplotlib.org/stable/gallery/statistics/boxplot_demo.html#sphx-glr-gallery-statistics-boxplot-demo-py
    # Fixing random state for reproducibility
    np.random.seed(19680801)

    # fake up some data
    spread = np.random.rand(50) * 100
    center = np.ones(25) * 50
    flier_high = np.random.rand(10) * 100 + 100
    flier_low = np.random.rand(10) * -100
    data = np.concatenate((spread, center, flier_high, flier_low))

    fig, ax = plt.subplots()

    bplot = ax.boxplot(data, patch_artist=True)
    for patch in bplot["boxes"]:
        patch.set_facecolor("pink")
    backstrip(ax)

    plt.savefig("/tmp/test_backstrip_v.png")


def test_backstrip_h():
    plt.clf()
    # adapted from https://matplotlib.org/stable/gallery/statistics/boxplot_demo.html#sphx-glr-gallery-statistics-boxplot-demo-py
    # Fixing random state for reproducibility
    np.random.seed(19680801)

    # fake up some data
    spread = np.random.rand(50) * 100
    center = np.ones(25) * 50
    flier_high = np.random.rand(10) * 100 + 100
    flier_low = np.random.rand(10) * -100
    data = np.concatenate((spread, center, flier_high, flier_low))

    fig, ax = plt.subplots()

    bplot = ax.boxplot(data, 0, "rs", 0, patch_artist=True)
    for patch in bplot["boxes"]:
        patch.set_facecolor("pink")
    backstrip(ax, orient="h")

    plt.savefig("/tmp/test_backstrip_h.png")


def test_backstrip_hatching():
    plt.clf()
    # adapted from https://seaborn.pydata.org/generated/seaborn.boxplot.html
    titanic = sns.load_dataset("titanic")
    ax = sns.boxplot(data=titanic, y="class", x="age", hue="alive", orient="h")
    backstrip(ax, hatch=["xx", "oo"], orient="h")

    plt.gcf().set_size_inches(10, 4)
    plt.savefig("/tmp/test_backstrip_hatching.png")


def test_backstrip_seaborn_v():
    plt.clf()
    # adapted from https://seaborn.pydata.org/generated/seaborn.boxplot.html
    titanic = sns.load_dataset("titanic")
    ax = sns.boxplot(data=titanic, x="class", y="age", hue="alive")
    backstrip(ax)

    plt.savefig("/tmp/test_backstrip_seaborn_v.png")


def test_backstrip_seaborn_h():
    plt.clf()
    # adapted from https://seaborn.pydata.org/generated/seaborn.boxplot.html
    titanic = sns.load_dataset("titanic")
    ax = sns.boxplot(data=titanic, y="class", x="age", hue="alive", orient="h")
    backstrip(ax, orient="h")

    plt.savefig("/tmp/test_backstrip_seaborn_h.png")


def test_backstrip_facetgrid_v():
    plt.clf()
    # adapted from https://seaborn.pydata.org/generated/seaborn.boxplot.html
    titanic = sns.load_dataset("titanic")
    g = sns.FacetGrid(titanic, margin_titles=True)
    g.map_dataframe(
        sns.boxplot,
        x="class",
        y="age",
        hue="alive",
        palette=sns.color_palette("tab10"),
    )
    for ax in g.axes.flat:
        backstrip(ax)

    plt.savefig("/tmp/test_backstrip_facetgrid_v.png")
