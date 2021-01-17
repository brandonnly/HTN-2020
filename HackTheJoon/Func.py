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
    linesNum = int(input("How many lines?"))
    var = {}
    for i in range(1, linesNum+1):
        var[i] = ([], [])

    with open(file, 'r') as csvfile:
        plots = csv.reader(csvfile, delimiter=',')
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
    plt.show()
    # plt.savefig('Line.png')


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
    plt.show()
    # plt.savefig('bar.png')


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
    plt.show()
    # plt.savefig('scatter.png')

def geo(file):
    data = read_csv(file)
    geoplotlib.dot(data, point_size=3)
    # geoplotlib.show()
    geoplotlib.savefig('img/map')


def geo_dot(file):      # file must have at top: name,lat,lon
    data = read_csv(file)
    geoplotlib.dot(data, point_size=3)
    # geoplotlib.show()
    geoplotlib.savefig('img/map')


def geo_spatial(file):
    data = read_csv(file)
    geoplotlib.graph(data, src_lat='lat_departure', src_lon='lon_departure', dest_lat='lat_arrival',
                     dest_lon='lon_arrival', color='hot_r', alpha=16, linewidth=2)
    geoplotlib.show()
#     geoplotlib.savefig('img/spatial')


type = input("What type of graph, geo, line, scatter or bar? ")

File = input("Input exact name with file type extension located within folder: ")
if ".xlsx" in File:
    read_file = pd.read_excel(File)
    File = read_file.to_csv('new.csv', index=None, header=True)

if type == "line":
    basic_line(File)

if type == "scatter":
    basic_scatter(File)

if type == "bar":
    basic_bar(File)

if type == "geo":
    geotype = input("What type? Dot Density? Spatial?")
    if geotype=="dot":
        geo_dot(File)

    if geotype=="spatial":
        geo_spatial(File)
    # Make sure to auto delete the image after the command in bot.py

if type == "geo":
    geo(File)

    # Make sure to auto delete the image after the command in bot.py
