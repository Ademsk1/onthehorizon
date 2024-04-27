from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt
from test import new_position

EARTH_R = 6.371e4


def get_coordinate_projection(lat, long, direction, distance, spacing):
    # lat, long and dir should be 0-360. 
    latR, longR, directionR = np.deg2rad([lat, long, direction])
    steps = np.arange(0, distance, spacing)
    latitudes = steps * np.cos(directionR) / EARTH_R + latR
    longitudes = steps * np.sin(directionR) / EARTH_R + longR
    return latitudes, longitudes



def main():
    start = np.array([51.5072,0.1276])
    lats, longs = get_coordinate_projection(start[0], start[1], 0, 3e6, 50)
    x = np.cos(lats) * np.cos(longs)
    y = np.cos(lats) *np.sin(longs)
    z = np.sin(lats)
    ax = plt.axes(projection='3d')
    ax.scatter(x[0], y[0], z[0])
    ax.plot3D(x,y,z)
    
    plt.show()


if __name__ == '__main__':
    main()