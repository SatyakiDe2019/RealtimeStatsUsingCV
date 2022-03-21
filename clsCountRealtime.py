##################################################
#### Written By: SATYAKI DE                   ####
#### Written On: 17-Jan-2022                  ####
#### Modified On 20-Mar-2022                  ####
####                                          ####
#### Objective: This python class will        ####
#### learn the number of coins stacks on      ####
#### top of another using computer vision     ####
#### with the help from Open-CV after         ####
#### manually recalibarting the initial       ####
#### data (Individual Coin Heights needs to   ####
#### adjust based on the distance of camera.) ####
##################################################

import cv2
from clsAutoDetector import *
import numpy as np
import os
import platform as pl

# Custom Class
from clsConfig import clsConfig as cf
import clsL as cl

# Initiating Log class
l = cl.clsL()

# Load Aruco detector
arucoParams = cv2.aruco.DetectorParameters_create()
arucoDict = cv2.aruco.Dictionary_get(cv2.aruco.DICT_5X5_50)

# Load Object Detector
detector = clsAutoDetector()

class clsCountRealtime:
    def __init__(self):
        self.sep = str(cf.conf['SEP'])
        self.Curr_Path = str(cf.conf['INIT_PATH'])
        self.coinDefH = float(cf.conf['COIN_DEF_HEIGHT'])
        self.pics2cm = float(cf.conf['PIC_TO_CM_MAP'])

    def learnStats(self, debugInd, var):
        try:
            # Per Coin Default Size from the known distance_to_camera
            coinDefH = self.coinDefH
            pics2cm = self.pics2cm

            # Load Cap
            cap = cv2.VideoCapture(0)
            cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
            cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

            while True:
                success, img = cap.read()

                if success == False:
                    break

                # Get Aruco marker
                imgCorners, a, b = cv2.aruco.detectMarkers(img, arucoDict, parameters=arucoParams)
                if imgCorners:

                    # Draw polygon around the marker
                    imgCornersInt = np.int0(imgCorners)
                    cv2.polylines(img, imgCornersInt, True, (0, 255, 0), 5)

                    # Aruco Perimeter
                    arucoPerimeter = cv2.arcLength(imgCornersInt[0], True)

                    # Pixel to cm ratio
                    pixelCMRatio = arucoPerimeter / pics2cm

                    contours = detector.detectObjects(img)

                    # Draw objects boundaries
                    for cnt in contours:
                        # Get rect
                        rect = cv2.boundingRect(cnt)
                        (x, y, w, h) = rect

                        print('*'*60)
                        print('Width Pixel: ')
                        print(str(w))
                        print('Height Pixel: ')
                        print(str(h))

                        # Get Width and Height of the Objects by applying the Ratio pixel to cm
                        objWidth = round(w / pixelCMRatio, 1)
                        objHeight = round(h / pixelCMRatio, 1)

                        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)

                        cv2.putText(img, "Width {} cm".format(objWidth), (int(x - 100), int(y - 20)), cv2.FONT_HERSHEY_PLAIN, 2, (100, 200, 0), 2)
                        cv2.putText(img, "Height {} cm".format(objHeight), (int(x - 100), int(y + 15)), cv2.FONT_HERSHEY_PLAIN, 2, (100, 200, 0), 2)

                        NoOfCoins = round(objHeight / coinDefH)

                        cv2.putText(img, "No Of Coins: {}".format(NoOfCoins), (int(x - 100), int(y + 35)), cv2.FONT_HERSHEY_PLAIN, 2, (250, 0, 250), 2)

                        print('Final Height: ')
                        print(str(objHeight))

                        print('No Of Coins: ')
                        print(str(NoOfCoins))

                cv2.imshow("Image", img)

                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break

            cap.release()
            cv2.destroyAllWindows()

            return 0
        except Exception as e:
            x = str(e)
            print('Error: ', x)

            return 1
