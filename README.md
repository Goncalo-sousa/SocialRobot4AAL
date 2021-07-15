# SocialRobot4AAL
![estg_h-01_png](https://user-images.githubusercontent.com/45467998/125843191-a854b410-923e-46f0-8636-4d9ba790ba6e.png)


This project was developed for the Computer Science Project of the Computer Engineering degree at the technology and Management School (ESTG) of the Polytechnic Institute of Leiria by the students Gonçalo Sousa and Élio Martins under the guidance of Professor António Manuel de Jesus Pereira and Professor Luís Alexandre Lopes Frazão. 


This project presents a systems integration, where it is possible to determine emotions from human faces, with some optimizations like discarding blurred photos.

With the next simple steps you will have the ability to replicate our integration.

**1. Install OpenCV**
- Install Python 
- In [Windows](https://www.geeksforgeeks.org/how-to-install-opencv-for-python-in-windows/) or [Linux](https://docs.opencv.org/master/d7/d9f/tutorial_linux_install.html)
> Warning: be careful with python environments!
- Download [file](https://github.com/opencv/opencv/blob/master/data/haarcascades/haarcascade_frontalface_default.xml) `haarcascade_frontalface_default.xml` pre-trained
---------------------------------------------------------------
**2. Install Node-RED**
- Create a virtual machine (optional)
- Install [Node-RED](https://nodered.org/docs/getting-started/)
---------------------------------------------------------------
**3. Install DeepFace**
- Create a virtual machine (optional)
- Clone the project [Deepface](https://github.com/serengil/deepface) belonging to Sefik Ilkin Serengil, and follow the steps: [README](https://github.com/serengil/deepface#readme)

> Can be installed on any operating system!
---------------------------------------------------------------
**4. Download Blurry Framework**
- Clone the project: [BlurryFrameRemover](https://github.com/deepshakes/BlurryFrameRemover)

> Install it on the same machine that has Node-RED!
---------------------------------------------------------------
**5. Files**
- Clone the files in: [repository](https://github.com/Goncalo-sousa/SocialRobot4AAL.git)

> File haarcascade_frontalface_default.xml must be in the same folder as cm.py! Or you need to change this line in the code: `face_cascade = cv2.CascadeClassifier('[Path to haarcascade_frontalface_default.xml]')` 
---------------------------------------------------------------
**6. Node-RED**
- Running Node-RED
- Open in your browser and import file `finalFlow.json` 

> Warning: You need to pay attention because in some widgets you will need to change their path!
