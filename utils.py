import matplotlib.pyplot as plt
import os


class PlotLine:
    def __init__(self, x: list, y: list, label: str):
        self.x = x
        self.y = y
        self.label = label


def plot(lines: list[PlotLine], x_title: str, y_title: str, title: str, file_name: str | None = None):
    """ Plot multiple lines inside a graph """

    # Config plot
    plt.title(title)
    plt.xlabel(x_title)
    plt.ylabel(y_title)

    # Insert lines in plot
    for line in lines:
        plt.plot(line.x, line.y, label=line.label)
    plt.legend()

    # Save the plot to a file
    if file_name:
        # Create the ./output folder if it doesn't exist
        if not os.path.exists("./output"):
            os.makedirs("./output")
        # Save file
        plt.savefig('./output/' + file_name)


if __name__ == '__main__':
    plot([
        PlotLine([1, 2, 3, 4, 5], [1, 2, 3, 4, 5], "line 1"),
        PlotLine([1, 2, 3, 4, 5], [3, 2, 1, 7, 9], "line 2"),
        PlotLine([1, 2, 3, 4, 5], [10, -5, 9, 1, 2], "line 3")
    ], "x axis", "y axis", "Graph title", "test")
