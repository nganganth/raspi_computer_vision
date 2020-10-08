import cv2, numpy
import os
import matplotlib.pyplot as plt

RTSP_URL = "rtsp://freja.hiof.no:1935/rtplive/_definst_/hessdalen03.stream"

class Test():
    def __init__(self):
        __location__ = os.path.realpath(
        os.path.join(os.getcwd(), os.path.dirname(__file__)))
        self.__filepath = os.path.join(__location__, 'images')
        self.__filename = "lake.tif"
        self.__fulldir = os.path.join(self.__filepath, self.__filename)
        if os.path.exists(self.__fulldir):
            print("OK!!!!!")
        else:
            print("Doesn't exit!!!")

    def showImage(self):
        img = cv2.imread(self.__fulldir, cv2.IMREAD_COLOR)
        cv2.imshow(self.__filename, img)
        cv2.waitKey(0)
        cv2.destroyWindow(self.__filename)
    
    def visualizeImage(self):
        img = cv2.imread(self.__fulldir, 1)
        plt.imshow(img)
        plt.title(self.__filename)
        plt.axis('off')
        plt.show()
    
    def showVideo(self):
        cap = cv2.VideoCapture(RTSP_URL)
        if not (cap.isOpened()):
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
        
    def saveVideo(self):
        cap = cv2.VideoCapture(RTSP_URL)

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
        location = os.path.realpath(
        os.path.join(os.getcwd(), os.path.dirname(__file__)))
        
        cap = cv2.VideoCapture(os.path.join(location, 'output.avi'))
        if os.path.exists(location):
            print("Existed")
        else:
            exit
        while(cap.isOpened()):
            ret, frame = cap.read()
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            cv2.imshow('frame', gray)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        
        cap.release()
        cv2.destroyAllWindows()
