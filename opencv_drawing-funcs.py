import cv2
import numpy as np 

# Create a black image
img = np.zeros((512,512,3), np.uint8)
# Draw a diagonal blue line with thickness of 5 px
cv2.line(img,(25,270),(475,475),(255,0,0),5) # Takes image, top-left and bottom-rigth coord. of line, color and thickness

cv2.rectangle(img,(254,254),(108,410),(0,255,0),3)  # Takes image, top-left and bottom-rigth coord. of rectangle, color and thickness

cv2.circle(img,(347,263), 63, (0,0,255), -1)    # Takes image, center of the circle, radius, color and if you wanna fill give -1 or decide thickness 
cv2.circle(img,(170,180), 36, (255,255,255), 4) # Takes image, center of the circle, radius, color and if you wanna fill give -1 or decide thickness 

pts = np.array([[25,8],[30,40],[70,35],[50,26]], np.int32)  # Create a numpy array
pts = pts.reshape((-1,1,2))                                 # reshape numpy array 
cv2.polylines(img,[pts],True,(0,255,255))                   # Takes image, array we want, if you wanna closed give True, if not give False and color


font = cv2.FONT_HERSHEY_SIMPLEX  # Choose font
cv2.putText(img,'Erkam',(100,100), font, 4,(255,0,255),2,cv2.LINE_AA) # image, text, position(bottom-left), font, font scale, color, thickness and Line Type. LINE_AA recommended by OPENCV !

if img is None:
    sys.exit("Could not read the img.")

cv2.imshow("Line Image", img)

# waitKey(0) waits forever if we press any key, code will finish and If also press "s-key" then save them to our code folder.
k = cv2.waitKey(0)
if k == ord("s"):
    cv2.imwrite("drawingfuncs-shapes.png", img)
