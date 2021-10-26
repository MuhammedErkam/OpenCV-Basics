import cv2
import numpy as np 

frame_width = 1280  
frame_height = 720

# Create a video - 0 means use your internal camera
cap = cv2.VideoCapture(0)

# Optional -- To set videos frame
cap.set(cv2.CAP_PROP_FRAME_WIDTH, frame_width)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, frame_height)

# Optional -- but it helps to get same speed when saving video 
fps = cap.get(cv2.CAP_PROP_FPS)

# Arrange Codec  -- h264, x264, avc1, xvid, mjpeg4 etc.
fourcc = cv2.VideoWriter_fourcc(*'h264')
# Arrange Properties of Video
out = cv2.VideoWriter('output.avi', fourcc, fps, (frame_width,frame_height),1)
out1 = cv2.VideoWriter('output1.avi', fourcc, fps, (frame_width,frame_height),0)

# last parameter of VideoWriter function is boolean and arranges color of video 
# out takes 1 as a last paramter and out1 takes 0 as last parameter.
# out will in BGR format and out1 will be in grayscale 
while(True):
    #ret is a boolean return value and frame is frames of video
    ret, frame = cap.read()
    #convert gray
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    #save frames to out
    out.write(frame)
    out1.write(gray)
    #show normal and gray videos
    cv2.imshow('frame',frame)
    cv2.imshow('gray',gray)

    #if pressed "q-key" finish video.
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

#release camera and saved video and kill all windows
cap.release()
out.release()
out1.release()
cv2.destroyAllWindows()


