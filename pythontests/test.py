import numpy as np
import matplotlib.pyplot as plt


r = 6.371e6
circumference = 2*np.pi * r

def new_position(position):
    #position comes in as geocordinates 0-360* 
    p1rad, p2rad = np.deg2rad(position[0]), np.deg2rad(position[1])
    dir = 45 # degrees
    dirRad = np.deg2rad(dir)
    step = 17 #17m 
    stepLat = step * np.cos(dirRad)
    stepLong = step*np.sin(dirRad)
    dLat = stepLat/r
    dLong = stepLong/r
    return [np.rad2deg(p1rad+dLat), np.rad2deg(p2rad + dLong)]


def main():
    starting_coordinates = np.array([51.5072,0.1276])
    size = 100000
    coordinates = np.empty(shape=(size, 2))
    coordinates[0] = starting_coordinates
    steps = np.linspace(0,size,size)
    print(coordinates[0])
    for i in range(1,size):
        new_coordinate = new_position(coordinates[i-1])
        coordinates[i] = new_coordinate
    print(coordinates[:100,0])
    plt.plot(steps,coordinates[:,0])
    plt.plot(steps,coordinates[:,1])

    plt.show()


if __name__ == '__main__':
    main()
    