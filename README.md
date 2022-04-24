# bacterial-motility
Automated analysis of bacterial motility assays

**main.py contains all the running code**

**calculate_param.py contains the calculation functions:**
  distance(self, coord_x, coord_y); takes in coordinates and calculates the pairwise distances
  distance_lr(self, coord_x, coord_y); takes in coordinates and calculates the pairwise distances with a sign (+/-) depending if cooridnates are left or right of x0
  conv_dist(self, dist_pixel); takes the distance in pixels is determines by the ruler calibration and calculates assumming 1 cm
  angle(self,height,dist,dist_conv_factor); takes the height y0, dist which are all the distances relative to x0, and dist_conv_factor obtained from conv_dist() to calculate the angle, theta
  
  
