import csv
import matplotlib.pyplot as plt
import geoplotlib
from geoplotlib.utils import read_csv


variables = {
    'x': [],
    'y': []
}

X = []
Y = []


def basic_line(file):
    """
    Renders a basic line graph
    :param file: path to file
    :return: saves image to temp/Line.png
    """
    lines_num = 2
    var = {}
    for i in range(1, lines_num+1):
        var[i] = ([], [])

    with open(file, 'r') as csvfile:
        plots = csv.reader(csvfile, delimiter=',')
        # Skip first line (values)
        lines_num = len(next(plots)) - 1
        next(plots)
        for row in plots:
            for j in range(1, len(row)):
                var[j][0].append(int(row[0]))
                var[j][1].append(int(row[j]))

    for k in range(lines_num):
        plt.plot(var[k+1][0], var[k+1][1])

    plt.xlabel('X')
    plt.ylabel('y')
    plt.legend()
    # plt.show()
    plt.savefig('temp/Line.png')


def basic_bar(file):
    """
    Renders a basic bar graph
    :param file: path to file
    :return: saves image to temp/bar.png
    """
    with open(file, 'r') as csvfile:
        plotting = csv.reader(csvfile, delimiter=',')
        next(plotting)
        for row in plotting:
            variables['x'].append(int(row[0]))
            variables['y'].append(int(row[1]))

    plt.bar(variables['x'], variables['y'], label='Bars1')

    plt.xlabel('X')
    plt.ylabel('y')
    plt.legend()
    # plt.show()
    plt.savefig('temp/bar.png')


def basic_scatter(file):
    """
    Renders a basic scatter graph
    :param file: path to file
    :return: saves image to temp/scatter.png
    """
    with open(file, 'r') as csvfile:
        plotting = csv.reader(csvfile, delimiter=',')
        next(plotting)
        for row in plotting:
            variables['x'].append(int(row[0]))
            variables['y'].append(int(row[1]))
    plt.scatter(variables['x'], variables['y'], label='Scatter', color='b')

    plt.xlabel('X')
    plt.ylabel('y')
    plt.legend()
    # plt.show()
    plt.savefig('temp/scatter.png')


def basic_pie(file):
    """
    Renders a basic pie graph
    :param file: path to file
    :return: saves image to temp/pie.png
    """
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
    plt.title('Pie Chart')
    plt.savefig('temp/pie.png')


def geo_dot(file):      # file must have at top: name,lat,lon
    """
    Renders a geo dot graph
    :param file: path to file
    :return: saves image to temp/map.png
    """
    data = read_csv(file)
    geoplotlib.dot(data, point_size=3)
    # geoplotlib.show()
    geoplotlib.savefig('temp/map')


def geo_spatial(file):
    """
    Renders a geo spatial graph
    :param file: path to file
    :return: saves image to temp/spatial.png
    """
    data = read_csv(file)
    geoplotlib.graph(data, src_lat='lat_departure', src_lon='lon_departure', dest_lat='lat_arrival',
                     dest_lon='lon_arrival', color='hot_r', alpha=16, linewidth=2)
    # geoplotlib.show()
    geoplotlib.savefig('temp/spatial')
