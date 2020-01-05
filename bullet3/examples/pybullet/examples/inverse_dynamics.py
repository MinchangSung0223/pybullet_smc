import pybullet as bullet
plot = True
import time
import os
import numpy as np
if (plot):
  import matplotlib.pyplot as plt
import math
from numpy.linalg import inv
verbose = False
import matplotlib.animation as animation
from matplotlib import style
# Parameters:
robot_base = [0., 0., 0.]
robot_orientation = [0., 0., 0., 1.]
delta_t = 0.001

# Initialize Bullet Simulator
id_simulator = bullet.connect(bullet.GUI)  # or bullet.DIRECT for non-graphical version
bullet.setTimeStep(delta_t)

# Switch between URDF with/without FIXED joints
with_fixed_joints = True

if with_fixed_joints:
  id_revolute_joints = [0, 3]
  id_robot = bullet.loadURDF("TwoJointRobot_h_fixedJoints.urdf",
                             robot_base,
                             robot_orientation,
                             useFixedBase=True)
else:
  id_revolute_joints = [0, 1]
  id_robot = bullet.loadURDF("TwoJointRobot_wo_fixedJoints.urdf",
                             robot_base,
                             robot_orientation,
                             useFixedBase=True)

bullet.changeDynamics(id_robot, -1, linearDamping=0, angularDamping=0)
bullet.changeDynamics(id_robot, 0, linearDamping=0, angularDamping=0)
bullet.changeDynamics(id_robot, 1, linearDamping=0, angularDamping=0)

jointTypeNames = [
    "JOINT_REVOLUTE", "JOINT_PRISMATIC", "JOINT_SPHERICAL", "JOINT_PLANAR", "JOINT_FIXED",
    "JOINT_POINT2POINT", "JOINT_GEAR"
]

# Disable the motors for torque control:
bullet.setJointMotorControlArray(id_robot,
                                 id_revolute_joints,
                                 bullet.VELOCITY_CONTROL,
                                 forces=[0.0, 0.0])
K = 1000*np.eye(2)
Lamda =700*np.eye(2)
Lamda[0,0] = 100
Gamma = 900*np.eye(5)

theta_hat = np.array([0,0,0,0,0])
s_time = 0.001;
tf = 20;
bullet.setGravity(0,0,-9.8)
q = np.transpose(np.array([0,0],dtype=float))
qdot = np.transpose(np.array([0,0],dtype=float))
qtwodot = np.transpose(np.array([0,0],dtype=float))

t = 0
pi = math.pi

style.use('fivethirtyeight')

fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)
xs = []
ys = []
while (1):
  t = t + 2*s_time
  qd = np.transpose(np.array([2*pi*t-math.sin(2*pi*t),2*pi*t-math.sin(2*pi*t)]))
  qd_dot = np.transpose(np.array([2*pi*(1-math.cos(2*pi*t)),2*pi*(1-math.cos(2*pi*t))]))
  qd_two_dot = np.transpose(np.array([4*pi*pi*math.sin(2*pi*t),4*pi*pi*math.sin(2*pi*t)]))

  #qd = np.transpose(np.array([0,pi/2],dtype=float))
  #qd_dot = np.transpose(np.array([0,0],dtype=float))
  #qd_two_dot = np.transpose(np.array([0,0],dtype=float))
 # print("q",q)
 # print("qdot",qdot)
 # print("qtwodot",qtwodot)
 # print("-------------------")
  #print("qd",qd)
 # print("qd_dot",qd_dot)
 # print("qd_two_dot",qd_two_dot)
  e = q-qd
  edot = qdot-qd_dot
  print("-------------------")
  print("e",e)
  print("edot",edot)
  print(np.matmul(Lamda,e))
  print(np.matmul(Lamda,np.reshape(e,(2,1))))

  v = qd_dot - np.matmul(Lamda,e);
  vdot = qd_two_dot-np.matmul(Lamda,edot);
 # print("-------------------")
 # print("v",v)
 # print("vdot",vdot)
  a = vdot;
  r = qdot-v;
 # print("-------------------")
 # print("a",a)
 # print("r",r)
  #torque = bullet.calculateInverseDynamics(id_robot, obj_pos, obj_vel, obj_acc)
  g = 9.806
  Y = np.zeros((2,5))
  Y[0,0] = a[0];
  Y[0,1] = math.cos(q[1])*(2*a[0]+a[1])-math.sin(q[1])*(qdot[1]*v[0]+qdot[0]*v[1]+qdot[1]*v[1]);
  Y[0,2] = a[1];
  Y[0,3] = g*math.cos(q[0]);
  Y[0,4] = g*math.cos(q[0]+q[1]);
  Y[1,0] = 0;
  Y[1,1] = math.cos(q[1])*a[0]+math.sin(q[1])*qdot[0]*v[0];
  Y[1,2] = a[0]+a[1];
  Y[1,3] = 0;
  Y[1,4] = g*math.cos(q[0]+q[1]);
 # print("-------------------")
 # print("Y",Y)
  theta_hat_dot = -np.matmul(np.matmul(inv(Gamma),np.transpose(Y)),r)
 # print("-------------------")
 # print("theta_hat_dot",theta_hat_dot)
  theta_hat = theta_hat+theta_hat_dot*s_time
  #print("-------------------")
  #print("theta_hat",theta_hat)
  r_ = np.reshape(r,(2,1))
  theta_hat_ = np.reshape(theta_hat,(5,1))
  u = np.matmul(Y,theta_hat_)-np.matmul(K,r_)
  print("q",q[0]*180/pi)
  print("-------------------\n")
  print("u",u)
  os.system('clear' )
  q[0]= bullet.getJointState(id_robot,0)[0]
  qdot[0]= bullet.getJointState(id_robot,0)[0]
  q[1] = bullet.getJointState(id_robot,3)[0]
  qdot[1] = bullet.getJointState(id_robot,3)[1]
  bullet.setJointMotorControlArray(id_robot,
                                   id_revolute_joints,
                                   bullet.TORQUE_CONTROL,
                                   forces=[0, 0])

  
  bullet.stepSimulation()
  #ax1.clear()
  #ax1.plot(xs, ys)
