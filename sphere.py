# inspiration code for Python Unit Testing Project

import math

# Function to calculate the volume of a cylinder
# Formula: Volume = π * r^3 * 4/3
def volume(rad):
    volume = math.pi * pow(rad, 3) * 4/3
    return volume

def prompt():
    print()
    print("------------------------------------------------------------")
    print("PYTHON PROGRAM TO FIND THE VOLUME OF A SPHERE")
    print("------------------------------------------------------------")
    radius = int(input("Please Enter the radius :"))
    print("\nThe Volume of a Cylinder = ", volume(radius))

if __name__ == '__main__':
    prompt()
