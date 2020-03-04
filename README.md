# Basic OpenCV Samples in Python

## Setup

### 1. Install Anaconda:  https://www.anaconda.com/distribution/

Steps: https://www.datacamp.com/community/tutorials/installing-anaconda-windows 

Run ff. command in prompt or terminal after install:
```
$ conda --version
$ conda update --all
```

### 2. Install OpenCV: 

In Linux:
```
$ conda install -c conda-forge opencv
```

In Windows: 

https://pysource.com/2019/03/15/how-to-install-python-3-and-opencv-4-on-windows/ 

Note: No need to reinstall Python, thus skip it. 

### 3. Try checking the OpenCV version after install:

```
$ python -c 'import cv2; print(cv2.__version__)'
```
In my case, this outputs 4.1.0

### 4. Run the sample codes in this repo:

- open_image
```Python
import cv2

img = cv2.imread("IOU.png",1)  # replace filename with your image
print("img.shape =", img.shape)
cv2.imshow("Sample Image", img)
cv2.waitKey(5000)
cv2.destroyAllWindows()

```

- open_video
```Python
import cv2

cap = cv2.VideoCapture('paper322-2019-11-29_07.26.37.mp4') # replace filename with your video

while(cap.isOpened()):
    ret, frame = cap.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    cv2.imshow('frame',gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
```

- open_webcam
```Python
# https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_gui/py_video_display/py_video_display.html

import cv2

cap = cv2.VideoCapture(0)

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    print("ret =", ret)

    # Display the resulting frame
    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
```

![](https://github.com/melvincabatuan/OpenCVSamplesPython/blob/master/webcam_demo/gray.png)

![](https://github.com/melvincabatuan/OpenCVSamplesPython/blob/master/webcam_demo/color.png)
