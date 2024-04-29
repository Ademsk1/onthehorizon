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
    coords = np.array([x,y,z])
    print(coords)
    rot = np.deg2rad(30)
    transform = np.array([
        [1, 0, 0 ],
        [0, np.cos(rot), np.sin(rot)],
        [0, -np.sin(rot), np.cos(rot)]
    ])

    xt, yt, zt = np.dot(transform, coords)

    #ax = plt.axes(projection='3d')
    # ax.scatter(x[0], y[0], z[0])
    #ax.plot3D(xt, yt, zt) 
    phi = np.linspace(0, 2*np.pi, 1000)
    plt.plot(np.sqrt(0.5 + (np.sin(phi)**2)*0.5))
    plt.plot(np.sqrt(2)/2 + (1-np.sqrt(2)/2)/2+np.sin(-(2*phi+np.pi/2))*(1-np.sqrt(2)/2)/2)

    
    plt.show()


if __name__ == '__main__':
    main()