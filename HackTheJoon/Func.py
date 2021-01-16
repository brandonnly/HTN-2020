import csv
import json
import numpy as np
import matplotlib.pyplot as plt


variables = {
    'x': [],
    'y': []
}

X=[]
Y=[]

def basic_line(file):
    linesNum = int(input("How many lines?"))
    x = []
    y = {

    }
    for num in range(linesNum):
        y[num+1] = []
    for i in range(linesNum):
        with open(file, 'r') as csvfile:
            Plotting = csv.reader(csvfile, delimiter=',')
            for row in Plotting:
                x.append(row[0])
                for j in range(1, len(row)):
                    y[j].append(row[j])
    for k in range(linesNum):
        # uses from object
        plt.plot(x, y[k+1])

    plt.xlabel('X')
    plt.ylabel('y')
    plt.legend()
    plt.show()

def basic_bar(file):
    with open(file, 'r') as csvfile:
        Plotting = csv.reader(csvfile, delimiter=',')
        for row in Plotting:
            variables['x'].append(int(row[0]))
            variables['y'].append(int(row[1]))

    plt.bar(variables['x'], variables['y'], label='Bars1')

    plt.xlabel('X')
    plt.ylabel('y')
    plt.legend()
    plt.show()
    # plt.savefig('BarGraph.png')


def basic_scatter(file):
    with open(file, 'r') as csvfile:
        Plotting = csv.reader(csvfile, delimiter=',')
        for row in Plotting:
            variables['x'].append(int(row[0]))
            variables['y'].append(int(row[1]))
    plt.scatter(variables['x'], variables['y'], label='Scatter', color='b')

    plt.xlabel('X')
    plt.ylabel('y')
    plt.legend()
    plt.show()
    # Save image
    # plt.savefig('Scatter.png')

    # basic_scatter('example.csv')
# basic_bar('example.csv')
# basic_line('example.csv')



type = input("What type of graph, line, scatter or bar? ")

File = input("Input exact name with file type extension located within folder: ")

if type == "line":
    basic_line(File)

if type == "scatter":
    basic_scatter(File)

if type == "bar":
    basic_bar(File)