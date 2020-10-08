import requests
from enum import Enum
from time import sleep
import cv2

class Cmd(Enum):
    LET = 'left'
    RIGHT = 'right'
    UP = 'up'
    DOWN = 'down'
    IN = 'zoomin'
    OUT = 'zoomout'
    SPEED = '45'

class CamController():
    def __init__(self, host, user, password):
        self.__url = "http://{}:{}@{}/web/cgi-bin/hi3510/".format(user, password, host) 
        self.__ptzctrl('stop')

    def ptz(self, cmd, sec):
        self.__ptzctrl(cmd.value)
        sleep(sec)
        self.__ptzctrl('stop')

    def preset(self, num):
        num = str(num - 1)
        requests.get("{}/preset.cgi?-act=goto&-number={}".format(self.__url, num))

    def __ptzctrl(self, cmdStr, speed):
        requests.get("{}/ptzctrl.cgi?-step=0&-act={}&-speed={}".format(self.__url, cmdStr, speed))

class CamMonitor():
    def __init__(int, host, user, password):
        self.__url = "rtsp://{}:554/user={}&password={}&channel=1&stream=0.sdp?".format(host, user, password)

    # def setup(self, cap):
    #     print('Current Width: ' + str(cap.get(3)))
    #     print('Current Height: ' + str(cap.get(4)))

    #     cap.set(3, 5000)
    #     cap.set(4, 5000)

    #     print('Updated Width: ' + str(cap.get(3)))
    #     print('Updated Height: ' + str(cap.get(4)))

    def capture(self):
        cap = cv2.VideoCapture(self.__url)
        # Check whether the selected camera is opened successfully
        if not (cap.isOpened())
            print('[Error]:Could not open camera!')
        while(True):
            # Capture frame-by-frame
            ret, frame = cap.read()

            # modify the captured image
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            # Display the resulting frame
            cv2.imshow('frame', frame)
            cv2.imshow('gray', gray)

            if cv2.waitKey(20) & 0xFF == ord('q'):
                break
        
        # When everyting done, release the capture
        cap.release()
        cv2.destroyAllWindows()
    
    def save(self):
        cap = cv2.VideoCapture(self.__url)

        # Define the codec and create VideoWriter object
        fourcc = cv2.VideoWriter_fourcc(*'XVID')
        out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640, 480))

        while(cap.isOpened()):
            ret, frame = cap.read()
            if ret == True:
                frame = cv2.flip(frame, 0)

                # Write the flipped frame
                out.write(frame)

                cv2.imshow('frame', frame)
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break
            else:
                break

        # Release out object after job is finished
        out.release()
        cap.release()
        cv2.destroyAllWindows()

    def playback(self):
        cap = cv2.VideoCapture('vtest.avi')
        while(cap.isOpened()):
            ret, frame = cap.read()
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            cv2.imshow('frame', gray)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        
        cap.release()
        cv2.destroyAllWindows()


