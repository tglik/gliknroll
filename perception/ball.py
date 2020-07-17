
import cv2
import numpy as np
import time

YELLOW_BALL_HSV_LOW = (20, 50, 50)
YELLOW_BALL_HSV_HIGH = (40, 255, 255)

SQRT2 = 2 ** 0.5

def identify_yellow_ball(frame):
    # Convert the frame to HSV colour model.
    frameHSV = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    # HSV values to define a colour range we want to create a mask from.
    # colorLow = np.array(YELLOW_BALL_HSV_LOW)
    # colorHigh = np.array(YELLOW_BALL_HSV_HIGH)
    # #print(colorLow, colorHigh)
    # mask = cv2.inRange(frameHSV, colorLow, colorHigh)
    # cv2.imshow("mask", mask)
    # contours, hierarchy = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    # contour_sizes = [(cv2.contourArea(contour), contour) for contour in contours]
    # biggest_contour = max(contour_sizes, key=lambda x: x[0])[1]
    
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    #gray = frameHSV[:, :, 2]#cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # gray = gray & mask 
    # blured = cv2.blur(gray, (2,2))
    #cv2.imshow("gray", gray)
    circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 2, 1,
              param1=100,
              param2=80,
              minRadius=5,
              maxRadius=0)
    #print(circles)
    fx = fy = fr = 0
    if circles is not None:
        stats = []
        
        min_v = float("inf")
        # find filled circle with the right color
        for (x, y, r) in circles[0]:
            rr = r / SQRT2
            b = (int(x-r), int(y-r), int(x+r), int(y+r))
            bb = (int(x-rr), int(y-rr), int(x+rr), int(y+rr))
            subimg = frameHSV[bb[1]:bb[3], bb[0]:bb[2]]
            if subimg.size > 0:
                if  230< x<250 and 320<y<340:
                    cv2.imshow("circle", subimg) 
                m, v = cv2.meanStdDev(subimg)
                if YELLOW_BALL_HSV_LOW[0]<=m[0][0]<=YELLOW_BALL_HSV_HIGH[0] and \
                   YELLOW_BALL_HSV_LOW[1]<=m[1][0]<=YELLOW_BALL_HSV_HIGH[1] and \
                   YELLOW_BALL_HSV_LOW[2]<=m[2][0]<=YELLOW_BALL_HSV_HIGH[2]:
                    stats.append((x,y,r,m[0][0],v[0][0]))
                    if min_v > v[0][0]:
                        fx = x
                        fy = y
                        fr = r
                        min_v = v[0][0]
            #cv2.circle(frame,(x,y),int(r),(0,0,255),2)
        #print([s for s in stats])# if  230< s[0]<250 and 390<s[1]<410 ])
    return x, y, z



if __name__ == "__main__":
    img = cv2.imread("/Users/tsahi/Downloads/WhatsApp Image 2020-07-17 at 10.51.43 AM (1).jpeg")
    ##img = cv2.imread("/Users/tsahi/Downloads/WhatsApp Image 2020-07-17 at 10.51.41 AM.jpeg")
    ##img = cv2.imread("/Users/tsahi/Downloads/WhatsApp Image 2020-07-17 at 10.51.39 AM.jpeg")
    ###img = cv2.imread("/Users/tsahi/Downloads/WhatsApp Image 2020-07-17 at 10.51.40 AM (1).jpeg")
    ###img = cv2.imread("/Users/tsahi/Downloads/WhatsApp Image 2020-07-17 at 10.51.47 AM (1).jpeg")
    ##img = cv2.imread("/Users/tsahi/Downloads/WhatsApp Image 2020-07-17 at 10.51.45 AM (1).jpeg")
    #img = cv2.imread("/Users/tsahi/Downloads/WhatsApp Image 2020-07-17 at 10.51.45 AM.jpeg")
    img = cv2.resize(img, (480, 640))
    x, y, r = identify_yellow_ball(img)
    print(x, y, r)
    cv2.circle(img,(x,y),int(r),(0,255,0),2)
    cv2.imshow('colorTest', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

