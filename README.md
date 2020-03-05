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

```
$ conda install -c conda-forge opencv
```

Sample in Windows: 

https://gist.github.com/melvincabatuan/dbd778e1cc276c38836c31ead4809856 

### 3. Try checking the OpenCV version after install:

```
$ python -c 'import cv2; print(cv2.__version__)'
```
In my case, this outputs 4.2

Build Info:
```shell
python opencv_version.py --build
```

```raw
(latest) D:\OpenCVSamplesPython>python opencv_version.py --build

prints OpenCV version

Usage:
    opencv_version.py [<params>]
    params:
        --build: print complete build info
        --help:  print this help


General configuration for OpenCV 4.2.0 =====================================
  Version control:               unknown

  Extra modules:
    Location (extra):            D:/bld/libopencv_1579753492509/work/opencv_contrib/modules
    Version control (extra):     unknown

  Platform:
    Timestamp:                   2020-01-23T04:31:21Z
    Host:                        Windows 10.0.14393 AMD64
    CMake:                       3.16.2
    CMake generator:             Ninja
    CMake build tool:            D:/bld/libopencv_1579753492509/_build_env/Library/bin/ninja.exe
    MSVC:                        1900
    Configuration:               Release

  CPU/HW features:
    Baseline:                    SSE SSE2 SSE3
      requested:                 SSE3
    Dispatched code generation:  SSE4_1 SSE4_2 FP16 AVX AVX2
      requested:                 SSE4_1 SSE4_2 AVX FP16 AVX2 AVX512_SKX
      SSE4_1 (14 files):         + SSSE3 SSE4_1
      SSE4_2 (1 files):          + SSSE3 SSE4_1 POPCNT SSE4_2
      FP16 (0 files):            + SSSE3 SSE4_1 POPCNT SSE4_2 FP16 AVX
      AVX (4 files):             + SSSE3 SSE4_1 POPCNT SSE4_2 AVX
      AVX2 (27 files):           + SSSE3 SSE4_1 POPCNT SSE4_2 FP16 FMA3 AVX AVX2

  C/C++:
    Built as dynamic libs?:      YES
    C++ Compiler:                C:/Program Files (x86)/Microsoft Visual Studio 14.0/VC/bin/amd64/cl.exe  (ver 19.0.24234.1)
    C++ flags (Release):         -MD -GL  /DWIN32 /D_WINDOWS /W4 /GR  /D _CRT_SECURE_NO_DEPRECATE /D _CRT_NONSTDC_NO_DEPRECATE /D _SCL_SECURE_NO_WARNINGS /Gy /bigobj /Oi  /fp:precise /FS     /EHa /wd4127 /wd4251 /wd4324 /wd4275 /wd4512 /wd4589 /MP2   /MD /O2 /Ob2 /DNDEBUG
    C++ flags (Debug):           -MD -GL  /DWIN32 /D_WINDOWS /W4 /GR  /D _CRT_SECURE_NO_DEPRECATE /D _CRT_NONSTDC_NO_DEPRECATE /D _SCL_SECURE_NO_WARNINGS /Gy /bigobj /Oi  /fp:precise /FS     /EHa /wd4127 /wd4251 /wd4324 /wd4275 /wd4512 /wd4589 /MP2   /MDd /Zi /Ob0 /Od /RTC1
    C Compiler:                  C:/Program Files (x86)/Microsoft Visual Studio 14.0/VC/bin/amd64/cl.exe
    C flags (Release):           -MD -GL  /DWIN32 /D_WINDOWS /W3  /D _CRT_SECURE_NO_DEPRECATE /D _CRT_NONSTDC_NO_DEPRECATE /D _SCL_SECURE_NO_WARNINGS /Gy /bigobj /Oi  /fp:precise /FS       /MP2    /MD /O2 /Ob2 /DNDEBUG
    C flags (Debug):             -MD -GL  /DWIN32 /D_WINDOWS /W3  /D _CRT_SECURE_NO_DEPRECATE /D _CRT_NONSTDC_NO_DEPRECATE /D _SCL_SECURE_NO_WARNINGS /Gy /bigobj /Oi  /fp:precise /FS       /MP2  /MDd /Zi /Ob0 /Od /RTC1
    Linker flags (Release):      /machine:x64  /INCREMENTAL:NO
    Linker flags (Debug):        /machine:x64  /debug /INCREMENTAL
    ccache:                      NO
    Precompiled headers:         NO
    Extra dependencies:
    3rdparty dependencies:

  OpenCV modules:
    To be built:                 aruco bgsegm calib3d ccalib core cvv datasets dnn dnn_objdetect dnn_superres dpm face features2d flann fuzzy gapi hfs highgui img_hash imgcodecs imgproc line_descriptor ml objdetect optflow phase_unwrapping photo plot python3 quality reg rgbd saliency shape stereo stitching structured_light superres surface_matching text tracking video videoio videostab xfeatures2d ximgproc xobjdetect xphoto
    Disabled:                    bioinspired world
    Disabled by dependency:      -
    Unavailable:                 cnn_3dobj cudaarithm cudabgsegm cudacodec cudafeatures2d cudafilters cudaimgproc cudalegacy cudaobjdetect cudaoptflow cudastereo cudawarping cudev freetype hdf java js matlab ovis python2 sfm ts viz
    Applications:                apps
    Documentation:               NO
    Non-free algorithms:         NO

  Windows RT support:            NO

  GUI:
    QT:                          YES (ver 5.12.1)
      QT OpenGL support:         NO
    Win32 UI:                    YES

  Media I/O:
    ZLib:                        D:/bld/libopencv_1579753492509/_h_env/Library/lib/z.lib (ver 1.2.11)
    JPEG:                        D:/bld/libopencv_1579753492509/_h_env/Library/lib/jpeg.lib (ver 90)
    WEBP:                        build (ver encoder: 0x020e)
    PNG:                         D:/bld/libopencv_1579753492509/_h_env/Library/lib/libpng.lib (ver 1.6.37)
    TIFF:                        D:/bld/libopencv_1579753492509/_h_env/Library/lib/tiff.lib (ver 42 / 4.1.0)
    JPEG 2000:                   build (ver 1.900.1)
    OpenEXR:                     build (ver 2.3.0)
    HDR:                         YES
    SUNRASTER:                   YES
    PXM:                         YES
    PFM:                         YES

  Video I/O:
    FFMPEG:                      YES (prebuilt binaries)
      avcodec:                   YES (58.54.100)
      avformat:                  YES (58.29.100)
      avutil:                    YES (56.31.100)
      swscale:                   YES (5.5.100)
      avresample:                YES (4.0.0)
    DirectShow:                  YES
    Media Foundation:            YES
      DXVA:                      YES

  Parallel framework:            Concurrency

  Trace:                         YES (with Intel ITT)

  Other third-party libraries:
    Intel IPP:                   2019.0.0 Gold [2019.0.0]
           at:                   D:/bld/libopencv_1579753492509/work/build/3rdparty/ippicv/ippicv_win/icv
    Intel IPP IW:                sources (2019.0.0)
              at:                D:/bld/libopencv_1579753492509/work/build/3rdparty/ippicv/ippicv_win/iw
    Lapack:                      YES (D:/bld/libopencv_1579753492509/_h_env/Library/lib/lapack.lib D:/bld/libopencv_1579753492509/_h_env/Library/lib/cblas.lib)
    Eigen:                       YES (ver 3.3.7)
    Custom HAL:                  NO
    Protobuf:                    build (3.5.1)

  Python 3:
    Interpreter:                 D:/bld/libopencv_1579753492509/_h_env/python (ver 3.7.6)
    Libraries:                   D:/bld/libopencv_1579753492509/_h_env/libs/python37.lib (ver 3.7.6)
    numpy:                       D:/bld/libopencv_1579753492509/_h_env/Lib/site-packages/numpy/core/include (ver 1.14.6)
    install path:                D:/bld/libopencv_1579753492509/_h_env/Lib/site-packages

  Python (for build):            D:/bld/libopencv_1579753492509/_h_env/python

  Java:
    ant:                         NO
    JNI:                         C:/Program Files/Java/zulu-8-azure-jdk_8.40.0.25-8.0.222-win_x64/include C:/Program Files/Java/zulu-8-azure-jdk_8.40.0.25-8.0.222-win_x64/include/win32 C:/Program Files/Java/zulu-8-azure-jdk_8.40.0.25-8.0.222-win_x64/include
    Java wrappers:               NO
    Java tests:                  NO

  Install to:                    D:/bld/libopencv_1579753492509/_h_env/Library
-----------------------------------------------------------------


Done
```

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

![](https://github.com/melvincabatuan/OpenCVSamplesPython/blob/master/open_image/SampleRun.png)

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

![](https://github.com/melvincabatuan/OpenCVSamplesPython/blob/master/open_video/SampleVid.png)

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
