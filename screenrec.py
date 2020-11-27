#numpy thu vien xu ly so
import cv2
import numpy as np
from PIL import ImageGrab

def screenRec():
    #defining the codec
    fourcc = cv2.VideoWriter_fourcc(*'XVID')

    #defining frame rate of the output video
    fps = 8.0

    #outputvideo
    out = cv2.VideoWriter('output.avi', fourcc, fps, (1366, 768))

    while(True):

        #take a snapshot of the screen using imagegrab
        img = ImageGrab.grab()

        #convert this image to array
        img_np = np.array(img)

        #display this frames as video
        win_title = "Screen Recorder"
        cv2.imshow(win_title, frame)

        #output the frame
        out.write(frame)

        #wait for 'q' key to stop recording(program)
        if(cv2.waitkey(1) & 0XFF == ord('q')):
            break

        #close the window and release recording
        out.release()

        #de-allocate any associated memory usage
        cv2.destroyAllWindows()

#call screenrec function
screenRec()