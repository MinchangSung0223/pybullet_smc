import pybullet as p
import time
import math
import os
import sys
import numpy as np
from datetime import datetime

clid = p.connect(p.SHARED_MEMORY)
if (clid < 0):
  p.connect(p.GUI)
  #p.connect(p.SHARED_MEMORY_GUI)

p.loadURDF("plane.urdf", [0.000000, 0.00000, -0.65+0.04])
p.loadURDF("table/table.urdf", 0.4500, 0.00000, -0.650000+0.04, 0.000000, 0.000000, 0.0, 1.0)
kukaId = p.loadURDF("indy5.urdf", [0, 0, 0])
#p.resetBasePositionAndOrientation(kukaId, [0, 0, 0], [0, 0, 0, 1])
p.resetBasePositionAndOrientation(kukaId, [0.0, 0, 0],
                                  [0.000000, 0.000000, 0.000000, 1.000000])
kukaEndEffectorIndex = 5
numJoints = p.getNumJoints(kukaId)-1

print(numJoints);
if (numJoints != 6):
  exit()

#lower limits for null space
ll = [-130/180*math.pi, -60/180*math.pi, -100/180*math.pi, -90/180*math.pi, -170/180*math.pi, -200/180*math.pi]
#upper limits for null space
ul = [130/180*math.pi, 150/180*math.pi, 80/180*math.pi, 180/180*math.pi, 170/180*math.pi, 200/180*math.pi]
#joint ranges for null space
jr = [4.6,3.6,3,4.7,6,7]
#restposes for null space
rp = [0, 0, math.pi/2, 0, math.pi/2, 0]
#joint damping coefficents
jd = [0.1, 0.1, 0.1, 0.1, 0.1, 0.1]

for i in range(numJoints):
  p.resetJointState(kukaId, i, rp[i])
objects = [p.loadURDF("mustard/mustard.urdf", [0.45000, 0, 0.2], [0.000000, 0.000000,0.000000,1.000000])]
p.setGravity(0, 0, -10)
t = 0.
prevPose = [0, 0, 0]
prevPose1 = [0, 0, 0]
hasPrevPose = 0
useNullSpace = 1

useOrientation = 1
#If we set useSimulation=0, it sets the arm pose to be the IK result directly without using dynamic control.
#This can be used to test the IK result accuracy.
useSimulation = 1
useRealTimeSimulation = 0
ikSolver = 0
p.setRealTimeSimulation(useRealTimeSimulation)
#trailDuration is duration (in seconds) after debug lines will be removed automatically
#use 0 for no-removal
trailDuration = 15
poses = np.array([0,0,0,0,0,0])
i=0
fov = 60
roll = 0
upAxisIndex = 2
camDistance = 4
pixelWidth = 640
pixelHeight = 480
nearPlane = 0.01
farPlane = 100
aspect = pixelWidth / pixelHeight
while 1:
  i+=1
  data = p.getLinkState(kukaId,kukaEndEffectorIndex,0,1)
  qutt = p.getEulerFromQuaternion(data[5]);
  
  
  x = data[0][0]
  y = data[0][1]
  z = data[0][2]
  yaw = qutt[0]
  pitch = qutt[1]
  roll  = qutt[2]
  M = np.zeros([3,3])
  M[0][0] = math.cos(yaw)*math.cos(pitch)
  M[0][1] = math.cos(yaw)*math.sin(pitch)*math.sin(roll)-math.sin(yaw)*math.cos(roll)
  M[0][2] = math.cos(yaw)*math.sin(pitch)*math.cos(roll)+math.sin(yaw)*math.sin(roll)
  M[1][0] = math.sin(yaw)*math.cos(pitch)
  M[1][1] = math.sin(yaw)*math.sin(pitch)*math.sin(roll)+math.cos(yaw)*math.cos(roll)
  M[1][2] = math.sin(yaw)*math.sin(pitch)*math.cos(roll)-math.cos(yaw)*math.sin(roll)
  M[2][0] = -math.sin(pitch)
  M[2][1] = math.cos(pitch)*math.sin(roll)
  M[2][2] = math.cos(pitch)*math.cos(roll)
  inverseM = np.linalg.inv(M)
  px = inverseM[0][0]*1+inverseM[0][1]*0+inverseM[0][2]*0
  py = inverseM[1][0]*0+inverseM[1][1]*1+inverseM[1][2]*0
  pz = inverseM[2][0]*0+inverseM[2][1]*0+inverseM[2][2]*1
 # print('eye : '+str(x)+','+str(y)+','+str(z))
 # print('target : '+str(px)+','+str(py)+','+str(pz))
  #viewMatrix = p.computeViewMatrix([x+0.15,y,z],[px,py,pz],[px,py,pz])
  viewMatrix = p.computeViewMatrixFromYawPitchRoll([x+0.15,y,z-0.35], -0.1,0,0,0, 1)
  projectionMatrix = p.computeProjectionMatrixFOV(fov, aspect, nearPlane, farPlane)
  rgbImage=p.getCameraImage(640,
                                      480,
                                      viewMatrix,
                                      projectionMatrix,
                                      shadow=1,
                                      lightDirection=[1, 1, 1],
                                      renderer=p.ER_BULLET_HARDWARE_OPENGL)

  if (useRealTimeSimulation):
    dt = datetime.now()
    t = (dt.second / 60.) * 2. * math.pi
  else:
    t = t + 0.01

  if (useSimulation and useRealTimeSimulation == 0):
    p.stepSimulation()

  for i in range(1):
   # pos = [0.3, 0.1 * math.cos(t), 0.3 + 0.1 * math.sin(t)]
    pos = [0.45, 0, 0.7+0.5]
    #end effector points down, not up (in case useOrientation==1)
    orn = p.getQuaternionFromEuler([0,0, 0])
          
    if (useNullSpace == 1):
      if (useOrientation == 1):
        jointPoses = p.calculateInverseKinematics(kukaId, kukaEndEffectorIndex, pos, orn)
      else:
        jointPoses = p.calculateInverseKinematics(kukaId,
                                                  kukaEndEffectorIndex,
                                                  pos
                                                  )
    else:
      if (useOrientation == 1):
        jointPoses = p.calculateInverseKinematics(kukaId,
                                                  kukaEndEffectorIndex,
                                                  pos,
                                                  orn,
                                                  jointDamping=jd,
                                                  solver=ikSolver,
                                                  maxNumIterations=100,
                                                  residualThreshold=.01)
      else:
        jointPoses = p.calculateInverseKinematics(kukaId,
                                                  kukaEndEffectorIndex,
                                                  pos,
                                                  solver=ikSolver)
   
    if (useSimulation):
      for i in range(numJoints):
        p.setJointMotorControl2(bodyIndex=kukaId,
                                jointIndex=i,
                                controlMode=p.POSITION_CONTROL,
                                targetPosition=jointPoses[i],
                                targetVelocity=0,
                                force=500,
                                positionGain=0.03,
                                velocityGain=1)
    else:
      #reset the joint state (ignoring all dynamics, not recommended to use during simulation)
      for i in range(numJoints-1):
        p.resetJointState(kukaId, i, jointPoses[i])
  #poses=np.hstack((poses,jointPoses))
  #np.save('poses.npy',poses)
  #np.save('/root/catkin_ws/src/dope/src/rgbimage.npy',rgbImage[2])
  #if(t>1.0 and t<1.01):
   # os.system('move_indy5 '+str(jointPoses[0])+' '+str(jointPoses[1])+' '+str(jointPoses[2])+' '+str(jointPoses[3])+' '+ str(jointPoses[4])+' '+str(jointPoses[5]) )
  #print(str(t)+' : '+str(data[1][0])+','+str(data[1][1])+','+str(data[1][2]) )
  ls = p.getLinkState(kukaId, kukaEndEffectorIndex)
  if (hasPrevPose):
    p.addUserDebugLine(prevPose, pos, [0, 0, 0.3], 1, trailDuration)
    p.addUserDebugLine(prevPose1, ls[4], [1, 0, 0], 1, trailDuration)
  prevPose = pos
  prevPose1 = ls[4]
  hasPrevPose = 1
p.disconnect()
