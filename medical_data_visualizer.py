import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Import data
df = pd.read_csv("medical_examination.csv")

# Add 'overweight' column
bmi = df["weight"] / ((df["height"] / 100) ** 2)
df["overweight"] = (bmi > 25).astype(int)

# Normalize data by making 0 always good and 1 always bad.
df["cholesterol"] = (df["cholesterol"] > 1).astype(int)
df["gluc"] = (df["gluc"] > 1).astype(int)


def draw_cat_plot():
    # Create DataFrame for cat plot using `pd.melt`
    df_cat = pd.melt(
        df,
        id_vars=["cardio"],
        value_vars=["cholesterol", "gluc", "smoke", "alco", "active", "overweight"],
    )

    # Group and reformat the data to split it by 'cardio'
    df_cat = (
        df_cat.groupby(["cardio", "variable", "value"])
        .size()
        .reset_index(name="total")
    )

    # Draw the catplot with 'sns.catplot()'
    fig = sns.catplot(
        data=df_cat,
        x="variable",
        y="total",
        hue="value",
        col="cardio",
        kind="bar",
    ).fig

    # Save image
    fig.savefig("catplot.png")
    return fig


def draw_heat_map():
    # Clean the data
    df_heat = df[
        (df["ap_lo"] <= df["ap_hi"])
        & (df["height"] >= df["height"].quantile(0.025))
        & (df["height"] <= df["height"].quantile(0.975))
        & (df["weight"] >= df["weight"].quantile(0.025))
        & (df["weight"] <= df["weight"].quantile(0.975))
    ]

    # Calculate the correlation matrix
    corr = df_heat.corr()

    # Generate a mask for the upper triangle
    mask = np.triu(np.ones_like(corr, dtype=bool))

    # Set up the matplotlib figure
    fig, ax = plt.subplots(figsize=(12, 12))

    # Draw the heatmap with 'sns.heatmap()'
    sns.heatmap(
        corr,
        mask=mask,
        annot=True,
        fmt=".1f",
        center=0,
        vmin=-0.16,
        vmax=0.32,
        square=True,
        linewidths=0.5,
        cbar_kws={"shrink": 0.5},
        ax=ax,
    )

    # Save image
    fig.savefig("heatmap.png")
    return fig
