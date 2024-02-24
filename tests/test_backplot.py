from matplotlib import pyplot as plt
import seaborn as sns

from backstrip import backplot


def test_backplot_v():
    plt.clf()
    # adapted from https://seaborn.pydata.org/generated/seaborn.boxplot.html
    titanic = sns.load_dataset("titanic")
    g = backplot(data=titanic, x="class", y="age", hue="alive", style="alive")
    assert g is not None

    plt.savefig("/tmp/test_backplot_v.png")


def test_backplot_v_facet():
    plt.clf()
    titanic = sns.load_dataset("titanic")
    g = backplot(
        data=titanic,
        x="class",
        y="age",
        hue="alive",
        col="who",
        style="alone",
    )
    assert g is not None

    plt.savefig("/tmp/test_backplot_v_facet.png")


def test_backplot_v_facet2():
    plt.clf()
    # adapted from https://seaborn.pydata.org/generated/seaborn.boxplot.html
    titanic = sns.load_dataset("titanic")
    g = backplot(
        data=titanic,
        x="class",
        y="age",
        hue="alive",
        col="alone",
        style="alive",
    )
    assert g is not None

    plt.savefig("/tmp/test_backplot_v_facet2.png")


def test_backplot_h():
    plt.clf()
    # adapted from https://seaborn.pydata.org/generated/seaborn.boxplot.html
    titanic = sns.load_dataset("titanic")
    backplot(
        data=titanic,
        y="class",
        x="age",
        hue="sex",
        style="alive",
        orient="h",
    )

    plt.savefig("/tmp/test_backplot_h.png")


def test_backplot_v_nox():
    plt.clf()
    # adapted from https://seaborn.pydata.org/generated/seaborn.boxplot.html
    titanic = sns.load_dataset("titanic")
    titanic["foo"] = "bar"
    backplot(
        data=titanic,
        y="age",
        style="alive",
        orient="v",
    )

    plt.savefig("/tmp/test_backplot_v_nox.png")


def test_backplot_v_nohue():
    plt.clf()
    # adapted from https://seaborn.pydata.org/generated/seaborn.boxplot.html
    titanic = sns.load_dataset("titanic")
    titanic["foo"] = "bar"
    backplot(
        data=titanic,
        y="age",
        # style="alive",
        orient="v",
        x="class",
    )

    plt.savefig("/tmp/test_backplot_v_nohue.png")
