###############################################
#### Written By: SATYAKI DE                ####
#### Written On: 17-Jan-2022               ####
#### Modified On 20-Mar-2022               ####
####                                       ####
#### Objective: This python script will    ####
#### auto-detects the contours of an image ####
#### using grayscale conversion & then     ####
#### share the contours details to the     ####
#### calling class.                        ####
###############################################

import cv2
from clsConfig import clsConfig as cf

class clsAutoDetector():
    def __init__(self):
        self.cntArea = int(cf.conf['CONTOUR_AREA'])

    def detectObjects(self, frame):
        try:
            cntArea = self.cntArea

            # Convert Image to grayscale Image
            grayImage = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            # Create a Mask with adaptive threshold
            maskImage = cv2.adaptiveThreshold(grayImage, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY_INV, 19, 5)

            cv2.imshow("Masked-Image", maskImage)

            # Find contours
            conts, Oth = cv2.findContours(maskImage, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

            objectsConts = []

            for cnt in conts:
                area = cv2.contourArea(cnt)
                if area > cntArea:
                    objectsConts.append(cnt)

            return objectsConts

        except Exception as e:
            x = str(e)
            print('Error: ', x)

            objectsConts = []

            return objectsConts
