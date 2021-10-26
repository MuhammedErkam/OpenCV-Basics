import cv2
import sys
# img is readed from samples file
# im2 is downloaded from internet and readed directly writing data path

img = cv2.imread(cv2.samples.findFile("starry_night.jpg"))
img2 = cv2.imread("/home/erkam/Downloads/download.png")

if img is None:
    sys.exit("Could not read the img.")
if img2 is None:
    sys.exit("Could not read the img2.")

cv2.imshow("Sample Image", img)
cv2.imshow("Opencv-logo Image", img2)

# waitKey(0) waits forever if we press any key, code will finish and If also press "s-key" then save them to our code folder.
k = cv2.waitKey(0)
if k == ord("s"):
    cv2.imwrite("starry_night.png", img)
    cv2.imwrite("opencv-logo.png", img2)