import os
import numpy as np
import cv2

class calcParam():
    #initializes attributes for this class
    def __init__(self):
        self.coord_x = []
        self.coord_y = []
        self.height=0
    #THIS FUNCTION CALCULATES THE DISTANCE IN PIXELS RELATIVE THE INITIAL POINT
#    def distance(self,coord_x,coord_y):
 #       for i in range(0,len(coord_x)-1):
  #          dist=np.sqrt((coord_x[i+1]-coord_x[0])**2 + (coord_y[i+1]-coord_y[0])**2)
  #      return dist


    def distance(self,coord_x,coord_y):
        dist_mat=[]
        for i in range(0,len(coord_x)-1):
            dist=np.sqrt((coord_x[i+1]-coord_x[0])**2 + (coord_y[i+1]-coord_y[0])**2)
            dist_mat.append(dist)
        return dist_mat

    def distance_lr(self,coord_x,coord_y): #for distances left and right of midpoint
        dist_mat2=[]
        for i in range(0,len(coord_x)-1):
            if ((coord_x[0]-coord_x[i+1] and coord_y[0]-coord_y[i+1]) > 0):
                dist=np.sqrt((coord_x[i+1]-coord_x[0])**2 + (coord_y[i+1]-coord_y[0])**2)
                dist_mat2.append(dist)
            else:
                dist = -np.sqrt((coord_x[i + 1] - coord_x[0]) ** 2 + (coord_y[i + 1] - coord_y[0]) ** 2)
                dist_mat2.append(dist)
        return dist_mat2
    #THIS FUNCTION CALCULATES THE CONVERSION FACTOR BASED ON A RULER IMAGE
    def conv_dist(self,dist_pixel):
        dist_cm=1/dist_pixel
        return dist_cm
    #THIS FUNCTION CALCULATES ANGLE THETA BETWEEN Y0 AND YN, WHERE YN IS THE DISTANCE TO THE ADJACENT PLATE
    def angle(self,height,dist,dist_conv_factor):
        theta = np.degrees(np.arctan((dist*dist_conv_factor)/height))
        return theta

