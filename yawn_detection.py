from scipy.spatial import distance as dist
from imutils.video import VideoStream
from imutils import face_utils
from threading import Thread
import numpy as np
import playsound
import argparse
import imutils
import time
import dlib
import cv2

class yawn_detection:
    def __init__(self, shape_predictor = None, alarm = None, webcam = None):
        
        #shape_predictor = self.shape_predictor
        #alarm = self.alarm
        #webcam = self.webcam

        self.shape_predictor = 'shape_predictor_68_face_landmarks.dat'
        self.alarm = 'alarm.wav'
        self.webcam = 'http://10.24.201.216:4747/mjpegfeed?640x480'

        # define two constants, one for the eye aspect ratio to indicate
        # blink and then a second constant for the number of consecutive
        # frames the eye must be below the threshold for to set off the
        # alarm
        self.MOUTH_AR_THRESH = 0.65
        self.MOUTH_AR_CONSEC_FRAMES = 15
        
        # initialize the frame counter as well as a boolean used to
        # indicate if the alarm is going off
        self.COUNTER = 0
        self.ALARM_ON = False

        self.detector = dlib.get_frontal_face_detector()
        self.predictor = dlib.shape_predictor(self.shape_predictor)   

        self.STATUS = False

        # grab the indexes of the facial landmarks for the mouth
        (self.Start, self.End) = face_utils.FACIAL_LANDMARKS_IDXS["mouth"]
    
    def mouth_aspect_ratio(self, mouth):
        #vertical dist (x-y)
        A = dist.euclidean(mouth[1], mouth[5])
        B = dist.euclidean(mouth[2], mouth[4])

        C = dist.euclidean(mouth[0], mouth[3])

        self.ratio = (A + B) / (2.0 * C)
        return self.ratio
    
    def sound_alarm(self, path):
        # play an alarm sound
	    playsound.playsound(path)

    def vs_loop(self):
        # start the video stream thread
        print("[INFO] starting video stream thread...")
        self.vs = VideoStream(src='http://10.24.201.216:4747/mjpegfeed?640x480').start()
        
        #print(self.vs.isOpened())
        time.sleep(1.0)

        while True:
            # grab the frame from the threaded video file stream, resize
            # it, and convert it to grayscale
            # channels)
            frame = self.vs.read()
            frame = imutils.resize(frame, width=450)
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            # detect faces in the grayscale frame
            self.rects = self.detector(gray, 0)

            # loop over the face detections
            for rect in self.rects:
                # determine the facial landmarks for the face region, then
                # convert the facial landmark (x, y)-coordinates to a NumPy
                # array
                shape = self.predictor(gray, rect)
                shape = face_utils.shape_to_np(shape)

                mouth = shape[self.Start:self.End]
                MAR = self.mouth_aspect_ratio(mouth)

                mouthHull = cv2.convexHull(mouth)
                cv2.drawContours(frame, [mouthHull], -1, (0, 255, 0), 1) #what do these numbers mean??

                if MAR < self.MOUTH_AR_THRESH:
                    self.COUNTER += 1

                    # if the eyes were closed for a sufficient number of
                    # then sound the alarm
                    if self.COUNTER >= self.MOUTH_AR_CONSEC_FRAMES:
                        self.STATUS = True
                        # draw an alarm on the frame
                        cv2.putText(frame, "DROWSINESS ALERT!", (10, 30),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
                    else:
                        self.STATUS = False
                else:
                    self.COUNTER = 0
                    ALARM_ON = False
                
                cv2.putText(frame, "MAR: {:.2f}".format(MAR), (300, 30),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)

            cv2.imshow("Frame", frame)
            key = cv2.waitKey(1) & 0xFF
        
            # if the `q` key was pressed, break from the loop
            if key == ord("q"):
                break


yawn = yawn_detection()
yawn.vs_loop()
