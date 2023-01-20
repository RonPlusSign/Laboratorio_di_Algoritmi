import random
import numpy as np
import csv

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

    total_iterations = 1_000
    for n in range(1, total_iterations + 1):
        number_of_nodes.append(n)

        # Randomly generate n distinct numbers
        # random_numbers = random.sample(range(1, total_iterations + 1), n)
        random_numbers = np.random.randint(0, 999, n)

        # Test binary search tree
        bst = BST()
        for number in random_numbers:
            bst.insert(number)
        depth_bst.append(bst.get_depth(bst.root))

        # Test red black tree
        rbt = RBT()
        for number in random_numbers:
            rbt.insert(number)
        depth_rbt.append(rbt.get_depth(rbt.root))

        if n % 1000 == 0:
            print("Tested performance with " + str(n) + " nodes")

    # Plot the performance results
    bst_line = PlotLine(number_of_nodes, depth_bst, "Binary Search Tree")
    rbt_line = PlotLine(number_of_nodes, depth_rbt, "Red Black Tree")

    # Create and save the plot
    plot([bst_line, rbt_line], "Number of nodes", "Number of layers", "Tree depth comparison", "insertion")

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
