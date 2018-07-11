from cpm import *
import matplotlib.pyplot as plt
import argparse
import warnings


def showExapmle():
    print("Showing example")
    example = CPM()
    example.add_node(1, p=3)
    example.add_node(2, p=2)
    example.add_node(3, p=2)
    example.add_node(4, p=1)
    example.add_node(5, p=4)
    example.add_node(6, p=1)
    example.add_node(7, p=2)

    example.add_edges_from([(1, 2), (1, 3), (3, 5), (5, 7), (2, 4), (4, 5), (4, 6), (6, 7)])

    example.drawGraph(filename="example.png")

    print(example.makespan)
    print(example.criticalPath.nodes())


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--file", help="load data from file")
    parser.add_argument("-n", "--nodes", help="load nodes with processing time", nargs="*", type=int)
    parser.add_argument("-e", "--edges", help="load edges between nodes", nargs="*", type=int)
    parser.add_argument("--example", help="show example", action="store_true")
    args = parser.parse_args()
    graph = CPM()
    if args.example:
        showExapmle()
    if args.nodes:
        for node, processing_time in zip(args.nodes[::2], args.nodes[1::2]):
            graph.add_node(node, p=processing_time)
    if args.edges:
        graph.add_edges_from(list(zip(args.edges[::2], args.edges[1::2])))
        print(graph.makespan)
        print(graph.criticalPath.nodes())

        graph.drawGraph(filename=args.file)


main()
