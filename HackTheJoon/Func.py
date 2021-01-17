import csv
import pandas as pd
import os
import numpy
import pyglet

import matplotlib.pyplot as plt
import geoplotlib
from geoplotlib.utils import read_csv


variables = {
    'x': [],
    'y': []
}

X=[]
Y=[]


def basic_line(file):
    linesNum = 2
    var = {}
    for i in range(1, linesNum+1):
        var[i] = ([], [])

    with open(file, 'r') as csvfile:
        plots = csv.reader(csvfile, delimiter=',')
        # Skip first line (values)
        linesNum = len(next(plots)) - 1
        next(plots)
        for row in plots:
            for j in range(1, len(row)):
                var[j][0].append(int(row[0]))
                var[j][1].append(int(row[j]))

    print(var)
    for k in range(linesNum):
        plt.plot(var[k+1][0], var[k+1][1])

    plt.xlabel('X')
    plt.ylabel('y')
    plt.legend()
    #plt.show()
    plt.savefig('temp/Line.png')


def basic_bar(file):
    with open(file, 'r') as csvfile:
        Plotting = csv.reader(csvfile, delimiter=',')
        next(Plotting)
        for row in Plotting:
            variables['x'].append(int(row[0]))
            variables['y'].append(int(row[1]))

    plt.bar(variables['x'], variables['y'], label='Bars1')
    print(variables)

    plt.xlabel('X')
    plt.ylabel('y')
    plt.legend()
    # plt.show()
    plt.savefig('temp/bar.png')


def basic_scatter(file):
    with open(file, 'r') as csvfile:
        Plotting = csv.reader(csvfile, delimiter=',')
        next(Plotting)
        for row in Plotting:
            variables['x'].append(int(row[0]))
            variables['y'].append(int(row[1]))
    plt.scatter(variables['x'], variables['y'], label='Scatter', color='b')

    plt.xlabel('X')
    plt.ylabel('y')
    plt.legend()
    #plt.show()
    plt.savefig('temp/scatter.png')


def basic_pie(file):
    names = []
    values = []
    with open(file, 'r') as csvfile:
        plotting = csv.reader(csvfile, delimiter=',')
        next(plotting)
        for row in plotting:
            names.append(row[0])
            values.append(row[1])
    colors = ['m', 'b', 'k', 'c', 'r']

    plt.pie(values, labels=names, colors=colors, startangle=90)
    plt.title(file.split('.')[0] + 'Pie Chart')
    plt.savefig('temp/pie.png')


def geo_dot(file):      # file must have at top: name,lat,lon
    data = read_csv(file)
    geoplotlib.dot(data, point_size=3)
    #geoplotlib.show()
    geoplotlib.savefig('temp/map.png')


def geo_spatial(file):
    data = read_csv(file)
    geoplotlib.graph(data, src_lat='lat_departure', src_lon='lon_departure', dest_lat='lat_arrival',
                     dest_lon='lon_arrival', color='hot_r', alpha=16, linewidth=2)
    #geoplotlib.show()
    geoplotlib.savefig('temp/spatial.png')
