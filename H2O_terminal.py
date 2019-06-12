import numpy as np
import os
import sys
water_data=sys.argv[1]
data=np.genfromtxt(fname=water_data, dtype='unicode', skip_header=2)
def bond_check (distance):
    if distance<1.5:
        print('True')
    elif distance==1.5:
        print('Maybe')
    else:
        print('False')
for num1 in range(0,3):
    title=data[num1,0]
    x1=float(data[num1,1])
    y1=float(data[num1,2])
    z1=float(data[num1,3])
    for num2 in range(0,3):
        if num1>num2:
            title2=data[num2,0]
            x2=float(data[num2,1])
            y2=float(data[num2,2])
            z2=float(data[num2,3])
            distance=np.sqrt((x2-x1)**2+(y2-y1)**2+(z2-z1)**2)
            bond_check(distance)
            water_dist=F'{title} to {title2} = {distance:.4}'
            print(water_dist)
