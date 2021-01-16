import csv
import json
import numpy as np
import matplotlib.pyplot as plt




X=[]
Y=[]


def basic_line(file,lines):
    X = []
    Y = []
    for i in range(lines):

        with open(file, 'r') as csvfile:
            Plotting = csv.reader(csvfile, delimiter=',')

            for row in Plotting:
                for i in range(len(row)):
                    if i==0:
                        X.append(int(row[i]))
                    if i%2 == 1:
                        Y.append(int(row[i]))




    plt.plot(X,Y, label='Loaded from file!')
    plt.xlabel('X')
    plt.ylabel('y')
    plt.legend()
    plt.show()

    # plt.savefig('LineGraph.png')



def basic_bar(file):
    with open(file, 'r') as csvfile:
        Plotting = csv.reader(csvfile, delimiter=',')
        for row in Plotting:
            X.append(int(row[0]))
            Y.append(int(row[1]))

    plt.bar(X,Y, label='Bars1')

    plt.xlabel('X')
    plt.ylabel('y')
    plt.legend()
    # plt.show()
    plt.savefig('BarGraph.png')


def basic_scatter(file):
    with open(file, 'r') as csvfile:
        Plotting = csv.reader(csvfile, delimiter=',')
        for row in Plotting:
            X.append(int(row[0]))
            Y.append(int(row[1]))
    plt.scatter(X,Y, label='Scatter', color='b')

    plt.xlabel('X')
    plt.ylabel('y')
    plt.legend()
    # plt.show()
    plt.savefig('Scatter.png')

    # basic_scatter('example.csv')
# basic_bar('example.csv')
# basic_line('example.csv')



type = input("What type of graph, line, scatter or bar? ")

File = input("Input exact name with file type extension located within folder: ")

if type == "line":
    linesNum = int(input("How many lines?"))
    basic_line(File,linesNum)

if type == "scatter":
    basic_scatter(File)

if type == "bar":
    basic_bar(File)