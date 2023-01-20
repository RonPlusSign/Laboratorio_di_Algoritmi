import random
from timeit import default_timer as timer
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
    execution_time_bst = []
    execution_time_rbt = []

    total_iterations = 10_000
    for n in range(1, total_iterations + 1):
        number_of_nodes.append(n)

        # Randomly generate n distinct numbers
        # random_numbers = random.sample(range(1, total_iterations + 1), n)
        random_numbers = np.random.randint(0, 999, n)

        # Test binary search tree
        bst = BST()
        start = timer()
        for number in random_numbers:
            bst.insert(number)
        end = timer()
        execution_time_bst.append((end - start) * 1_000)  # In milliseconds

        # Test red black tree
        rbt = RBT()
        start = timer()
        for number in random_numbers:
            rbt.insert(number)
        end = timer()
        execution_time_rbt.append((end - start) * 1_000)  # In milliseconds

        if n % 1000 == 0:
            print("Tested performance with " + str(n) + " nodes")

    # Plot the performance results
    bst_line = PlotLine(number_of_nodes, execution_time_bst, "Binary Search Tree")
    rbt_line = PlotLine(number_of_nodes, execution_time_rbt, "Red Black Tree")

    # Plot linear graph (y=x)
    # linear_line = PlotLine(number_of_nodes, number_of_nodes, "y = x")

    # Plot logarithm graph (y= log(x))
    # logarithmic_line = PlotLine(number_of_nodes, [log(i) for i in number_of_nodes], "y = log(x)")

    # Create and save the plot
    plot([bst_line, rbt_line],  # , linear_line, logarithmic_line],
         "Number of nodes", "Execution time (ms)", "Insertion performance", "insertion")

    print("Plot saved")

    # Save data to csv file
    with open("./output/insertion.csv", "w", newline='') as output:
        writer = csv.writer(output)
        writer.writerow(["Number of nodes", "Binary Search Tree", "Red Black Tree"])

        for i in range(len(number_of_nodes)):
            writer.writerow([number_of_nodes[i], execution_time_bst[i], execution_time_rbt[i]])

    print("CSV saved")


if __name__ == '__main__':
    main()
