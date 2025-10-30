import matplotlib.pyplot as plt
from src.io_utils import *
from src.metrics import *

# Plot per categories
def plot_per_category(df: pd.DataFrame):
    fig, ax = plt.subplots(figsize=(7,5))
    ax.bar(df["category"], df["revenue"], 
           color="#6495ED", width=0.7)
    ax.set_title("Revenue per category")
    ax.set_xlabel("Category")
    ax.set_ylabel("Revenue")
    ax.grid(True, axis="y", alpha=0.5)
    plt.xticks(rotation=45)
    plt.tight_layout()
    return fig

def plot_per_city(df: pd.DataFrame):
    fig, ax = plt.subplots(figsize=(7,5))
    ax.bar(df["city"], df["revenue"], 
           color="#4682B4", width=0.7)
    ax.set_title("Revenue per city")
    ax.set_xlabel("City")
    ax.set_ylabel("Revenue")
    ax.grid(True, axis="y", alpha=0.5)
    plt.xticks(rotation=45)
    plt.tight_layout()
    return fig

def line(ax, x, y, title, xlabel, ylabel, grid: bool = True):

    ax.plot(x, y, marker="o")
    ax.set_title(title)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.grid(grid, axis="y", alpha=0.5)
    return ax