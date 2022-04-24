import os
import numpy as np
import cv2
import matplotlib.pyplot as plt
from calculate_param import *
from clickit import *
import random as rd
from IPython import get_ipython;

yo=[]
x_coord=[]
y_coord=[]
angle_plot=[]
x_coord_ruler=[]
y_coord_ruler=[]
test = clickIt()
dist_i=[]
m = calcParam()
yo1=[]
yo2=[]
#test.getCoord()

#CALCULATES THE DISTANCE RELATVIVE TO THE FIRST CLICK; ALTERNATIVELY, WE SHOULD CALUCLATE THE DISTANCE FROM THE CENTER OF THE PICTURE
for i in range(4):
    #PICK TWO POINTS THAT DEFINE THE RULER SIZE
    if i == 0 or i == 1:
        yo.append(test.getCoord())
        x_coord_ruler.append(yo[i][0])
        y_coord_ruler.append(yo[i][1])
        plt.scatter(x_coord_ruler,y_coord_ruler)
        im=plt.imread(r"C:\Users\trevo\OneDrive\Desktop\test.jpg")
        implot=plt.imshow(im)
        plt.show()
    #PICK THE POINT WHERE ALL THE POINTS WILL BE CALULATED FROM
    elif i == 2: #START FROM CENTER OF THE PICTURE
        yo1.append(test.getCoord())
        x_coord.append(yo1[i-2][0])
        y_coord.append(yo1[i-2][1])
        plt.scatter(x_coord, y_coord)
        im = plt.imread(r"C:\Users\trevo\OneDrive\Desktop\test.jpg")
        implot = plt.imshow(im)
        plt.show()
    #    im = plt.imread(r"C:\Users\trevo\OneDrive\Desktop\test.jpg")
    #    x_coord.append(len(im[0])/2)
     #   y_coord.append(len(im[:,0])/2)
    #ALL OTHER POINTS
    else:
        yo2.append(test.getCoord())
        x_coord.append(yo2[i-3][0])
        y_coord.append(yo2[i-3][1])
        plt.scatter(x_coord, y_coord)
        im = plt.imread(r"C:\Users\trevo\OneDrive\Desktop\test.jpg")
        implot = plt.imshow(im)
        plt.show()
        #x_coord.append(rd.randint(0,200))
        #y_coord.append(rd.randint(0,300))
    #plt.scatter(x_coord,y_coord)
    #im=plt.imread(r"C:\Users\trevo\OneDrive\Desktop\ruler.jpg")
    #implot=plt.imshow(im)
    #plt.show()

#CALCULATE THE DISTANCES HERE
m_dist_ruler=m.distance(x_coord_ruler, y_coord_ruler)

#CALCULATE THE DISTANCE WITH SIGN BASED ON THE LEFT OR RIGHT WITH RESPECT TO X0 POSITION
m_dist=m.distance_lr(x_coord, y_coord)


#CALCULATE THE CONVERSION FACTOR FOR CM/PIXEL

dist_conv = m.conv_dist(m_dist_ruler[0])

#PICK A HEIGHT IN CM

height=20

#CALCULATE ANGLE BASED ON A REAL HEIGHT, WITHOUT REAL HEIGHT, ANGLE IS ARBITRARY
for i in range(0,len(m_dist)):
    angle_plot.append(m.angle(float(height),m_dist[i],dist_conv))
print(angle_plot)

#CONVERTS PIXEL DISTANCES TO CM

converted_m_dist = []
for i in range(0,len(m_dist)):
    converted_m_dist.append(m_dist[i]*dist_conv)

#JUST IGNORE THIS FOR NOW
#for i in range(0,len(angle_plot)):
    #y_n.append(converted_m_dist[i]/np.cos(angle_plot[i]))
    #y_n.append(height / np.cos(angle_plot[i]))

#PLOTS THE DISTANCE FROM X0 AGAINST THE DISTANCE
plt.scatter(converted_m_dist,angle_plot)

#plt.scatter(angle_plot,y_n)

plt.ylabel("Angle, θ (degrees)")
plt.xlabel("Distance from X0 (cm)")
plt.show()

quit()


#THIS PART IS TO JUST RANDOM SHIT THAT MIGHT BE USEFUL
#get_ipython().magic('reset -sf')

angle_plot2=[]
lr_mdist=m.distance_lr(x_coord, y_coord)
for i in range(0,len(lr_mdist)):
    angle_plot2.append(m.angle(float(100),lr_mdist[i],dist_conv))
#print(angle_plot2)
converted_m_dist_lr = []
for i in range(0,len(lr_mdist)):
    #converted_m_dist_lr.append(lr_mdist[i]*dist_conv)
    converted_m_dist_lr.append(lr_mdist[i] * dist_conv)
#print(converted_m_dist_lr)

print(converted_m_dist_lr == converted_m_dist)
plt.scatter(converted_m_dist_lr,angle_plot2)
plt.ylabel("Angle, θ (degrees)")
plt.xlabel("Distance from center (cm)")
plt.show()
#(m.angle(12,m_dist,dist_conv))



# See PyCharm help at https://www.jetbrains.com/help/pycharm/
