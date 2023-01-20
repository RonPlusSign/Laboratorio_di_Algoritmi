import random
import numpy as np
import csv
import sys
from math import log2

from binary_search_tree import BST
from red_black_tree import RBT
from utils import PlotLine, plot


def main():
    """ Test the performance of Binary Search Trees and Red Black Trees
    Plot the performance results in a graph, saving it to the ./output folder
    """

    number_of_nodes = []
    depth_bst = []
    depth_rbt = []
    logarithm_values = []

    max_nodes = 5_000
    # sys.setrecursionlimit(max_nodes + 1)	# Needed in the worst case, where the depth might increase linearly and get_depth() won't work

    for n in range(1, max_nodes + 1, 100):
        number_of_nodes.append(n)
        logarithm_values.append(log2(n))

        # Randomly generate n distinct numbers
        random_values = np.random.randint(0, 999, n)

        # Worst case for BST: numbers in order
        worst_case_values = np.arange(1, n + 1, step=1)

        # Best case for BST: numbers perfectly balanced
        interval = [i for i in range(1, n + 1)]
        best_case_values = []
        while len(interval) > 0:
            best_case_values.append(interval.pop(int(len(interval) / 2)))

        # Choose used values and result title
        values = random_values
        title = "random"

        # Test binary search tree
        bst = BST()
        for number in values:
            bst.insert(number)
        depth_bst.append(bst.get_depth(bst.root))

        # Test red black tree
        rbt = RBT()
        for number in values:
            rbt.insert(number)
        depth_rbt.append(rbt.get_depth(rbt.root))

        if n % 1000 == 0:
            print("Tested performance with " + str(n) + " nodes")

    # Plot the performance results
    bst_line = PlotLine(number_of_nodes, depth_bst, "Binary Search Tree")
    rbt_line = PlotLine(number_of_nodes, depth_rbt, "Red Black Tree")
    logarithm_line = PlotLine(number_of_nodes, logarithm_values, "y = log(x)")

    # Create and save the plot
    plot([bst_line, rbt_line, logarithm_line],
         "Tree depth comparison",
         "Number of nodes",
         "Number of layers",
         "insertion")

    print("Plot saved")

    # Save data to csv file
    with open("./output/insertion.csv", "w", newline='') as output:
        writer = csv.writer(output)
        writer.writerow(["Nodes", "Depth (BST)", "Depth (RBT)"])

        for i in range(len(number_of_nodes)):
            writer.writerow([number_of_nodes[i], depth_bst[i], depth_rbt[i]])
        print("CSV saved")


if __name__ == '__main__':
    main()
