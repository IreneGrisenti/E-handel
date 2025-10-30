import matplotlib.pyplot as plt
from src.io_utils import *
from src.metrics import *

# Function for bar plot
def bar(ax, x, y, title, xlabel, ylabel, color, grid: bool = True):
    ax.bar(x, y, color=color)
    ax.set_title(title)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.grid(grid, axis="y", alpha=0.5)
    plt.xticks(rotation=45)
    return ax

# Function for line plots
def line(ax, x, y, title, xlabel, ylabel, label=None, grid: bool = True):
    ax.plot(x, y, marker="o", label=label, color="#6495ED")
    ax.set_title(title)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.grid(grid, axis="y", alpha=0.5)
    return ax

# Function for scatter plots
def scatter(ax, x, y, title, xlabel, ylabel, grid: bool = True):
    ax.scatter(x, y, alpha=0.5, color="#335DAA")
    ax.set_title(title)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.grid(grid, alpha=0.5)
    return ax

# Function for box plots
def box_p(ax, data, labels, title, xlabel, grid: bool = True):
    ax.boxplot(data, vert=False)
    ax.set_yticklabels(labels)
    ax.set_title(title)
    ax.set_xlabel(xlabel)
    ax.grid(grid, axis="x")
    return ax