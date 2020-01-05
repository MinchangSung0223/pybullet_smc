import matplotlib.pyplot as plt
import numpy as np
import pybullet as p
import time
import cv2

direct = p.connect(p.GUI)  #, options="--window_backend=2 --render_device=0")
#egl = p.loadPlugin("eglRendererPlugin")

p.loadURDF('plane.urdf')
p.loadURDF('banana/object_1.urdf', basePosition=[0.0, 0.0, 0.5],baseOrientation=p.getQuaternionFromEuler([0.5,0,0]))
width = 640
height = 640

fov = 60
aspect = width / height
near = 0.02
far = 1

view_matrix = p.computeViewMatrix([0, 0, 0.5], [0, 0, 0], [1, 0, 0])
projection_matrix = p.computeProjectionMatrixFOV(fov, aspect, near, far)
p.setRealTimeSimulation(1)
p.setGravity(0, 0, -10)
for i in range(0,1000):
 p.stepSimulation()

time.sleep(1)
# Get depth values using the OpenGL renderer
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


viewMat = [
    0.642787516117096, -0.4393851161003113, 0.6275069713592529, 0.0, 0.766044557094574,
    0.36868777871131897, -0.5265407562255859, 0.0, -0.0, 0.8191521167755127, 0.5735764503479004,
    0.0, 2.384185791015625e-07, 2.384185791015625e-07, -5.000000476837158, 1.0
]
projMat = [
    0.7499999403953552, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, -1.0000200271606445, -1.0,
    0.0, 0.0, -0.02000020071864128, 0.0
]
# Plot both images - should show depth values of 0.45 over the cube and 0.5 over the plane
print(depth_opengl)
np.save("depth.npy",depth_buffer_opengl )
cv2.imwrite('depth.png',np.uint8(depth_opengl*255))
plt.subplot(1, 3, 1)
plt.imshow(depth_opengl, cmap='gray', vmin=0, vmax=1)
plt.title('Depth OpenGL3')

plt.subplot(1, 3, 2)
plt.imshow(rgb_opengl)
plt.title('RGB OpenGL3')


plt.subplot(1, 3, 3)
plt.imshow(seg_opengl)
plt.title('Seg OpenGL3')

plt.subplots_adjust(hspace=1)

plt.show()
