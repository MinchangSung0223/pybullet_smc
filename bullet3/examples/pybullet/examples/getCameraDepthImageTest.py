import matplotlib.pyplot as plt
import numpy as np
import pybullet as p
import time
import cv2
import math
direct = p.connect(p.GUI)  #, options="--window_backend=2 --render_device=0")
#egl = p.loadPlugin("eglRendererPlugin")
randx = np.random.rand(1)*20-10
randy = np.random.rand(1)*20-10
randd = (np.random.rand(1)*180-90)/1000
rando = np.random.rand(1)*15-7.5


objId = p.loadURDF('banana/object_1.urdf', basePosition=[0.0, 0.0, 0],baseOrientation=p.getQuaternionFromEuler([(33.9+randx )/180*math.pi,(25.5+randy)/180*math.pi,0]))

width = 640
height = 640

fov = 60
aspect = width / height
near = 0.02
far = 5



p.setRealTimeSimulation(1)
p.setGravity(0, 0, 0)
for i in range(0,1000):
 p.stepSimulation()
rand_ox = np.random.rand(1)*360-180
rand_oy = np.random.rand(1)*360-180
rand_oz = np.random.rand(1)*360-180
randtheta = np.random.rand(1)*math.pi*2 - math.pi
randpsi = np.random.rand(1)*math.pi*2 - math.pi
r = 0.9
for i in range(0,500):
   randx = np.random.rand(1)*20-10
   randy = np.random.rand(1)*20-10
   randd = (np.random.rand(1)*180-90)/1000
   rando = np.random.rand(1)*15-7.5
   
# Get depth values using the OpenGL renderer
   p.resetBasePositionAndOrientation(objId,[0,0,0],p.getQuaternionFromEuler([(33.9+randx )/180*math.pi,(25.5+randy)/180*math.pi,0]))
   view_x = r*math.cos(randtheta)*math.cos(randpsi)
   view_y = r*math.sin(randtheta)*math.cos(randpsi)
   view_z = r*math.sin(randpsi)
   view_matrix = p.computeViewMatrix([view_x, view_y, view_z], [0, 0, 0], [-view_x, view_y, view_z])
   #view_matrix = p.computeViewMatrixFromYawPitchRoll([0,0,0],0.9+randd,0,0,0,1)
   projection_matrix = p.computeProjectionMatrixFOV(fov, aspect, near, far)
   images = p.getCameraImage(width,
                          height,
                          view_matrix,
                          projection_matrix,
                          shadow=True,
                          renderer=p.ER_BULLET_HARDWARE_OPENGL)
   rgb_opengl = np.reshape(images[2], (height, width, 4)) * 1. / 255.
   depth_buffer_opengl = np.reshape(images[3], [width, height])
   depth_opengl = far * near / (far - (far - near) * depth_buffer_opengl)
   seg_opengl = np.reshape(images[4], [width, height]) * 1. / 255.


# Plot both images - should show depth values of 0.45 over the cube and 0.5 over the plane
   print(depth_opengl)
   filename = "depth_"+str(randtheta[0])+"_"+str(randpsi[0])+"_"+str(i)+".npy"
   np.save(filename,depth_buffer_opengl )
   cv2.imwrite('depth.png',np.uint8(depth_opengl*255))
