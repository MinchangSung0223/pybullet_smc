import pybullet as bullet
plot = True
import time
import numpy as np
if (plot):
  import matplotlib.pyplot as plt
import math
verbose = False

# Parameters:
robot_base = [0., 0., 0.]
robot_orientation = [0., 0., 0., 1.]
delta_t = 0.0001

# Initialize Bullet Simulator
id_simulator = bullet.connect(bullet.GUI)  # or bullet.DIRECT for non-graphical version
bullet.setTimeStep(delta_t)

# Switch between URDF with/without FIXED joints
with_fixed_joints = True

if with_fixed_joints:
  id_revolute_joints = [0, 3]
  id_robot = bullet.loadURDF("TwoJointRobot_w_fixedJoints.urdf",
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

# Target Positions:
start = 0.0
end = 5.0

steps = int((end - start) / delta_t)
t = [0] * steps
q_pos_desired = [[0.] * steps, [0.] * steps]
q_vel_desired = [[0.] * steps, [0.] * steps]
q_acc_desired = [[0.] * steps, [0.] * steps]

for s in range(steps):
  t[s] = start + s * delta_t
  q_pos_desired[0][s] = math.sin(2*math.pi*t[s])
  q_pos_desired[1][s] = math.sin(2*math.pi*t[s])

  q_vel_desired[0][s] = 2*math.pi*(math.cos(2*math.pi*t[s]))
  q_vel_desired[1][s] = 2*math.pi*(math.cos(2*math.pi*t[s]))

  q_acc_desired[0][s] = 4*math.pi*math.pi*math.sin(2*math.pi*t[s])
  q_acc_desired[1][s] = 4*math.pi*math.pi*math.sin(2*math.pi*t[s])

q_pos = [[0.] * steps, [0.] * steps]
q_vel = [[0.] * steps, [0.] * steps]
q_tor = [[0.] * steps, [0.] * steps]
theta_hat = [0,0,0,0,0]

# Do Torque Control:
for i in range(len(t)):

  # Read Sensor States:
  joint_states = bullet.getJointStates(id_robot, id_revolute_joints)

  q_pos[0][i] = joint_states[0][0]
  a = joint_states[1][0]
  if (verbose):
    print("joint_states[1][0]")
    print(joint_states[1][0])
  q_pos[1][i] = a

  q_vel[0][i] = joint_states[0][1]
  q_vel[1][i] = joint_states[1][1]

  # Computing the torque from inverse dynamics:
  obj_pos = [q_pos[0][i], q_pos[1][i]]
  obj_vel = [q_vel[0][i], q_vel[1][i]]
  obj_acc = [q_acc_desired[0][i], q_acc_desired[1][i]]
  if (verbose):
    print("calculateInverseDynamics")
    print("id_robot")
    print(id_robot)
    print("obj_pos")
    print(obj_pos)
    print("obj_vel")
    print(obj_vel)
    print("obj_acc")
    print(obj_acc)
  e  =[q_pos_desired[0][i]-q_pos[0][i], q_pos_desired[1][i]-q_pos[1][i]]
  edot  =[q_vel_desired[0][i]-q_vel[0][i],q_vel_desired[1][i]-q_vel[1][i]]
  v = [q_vel_desired[0][i]-20*e[0],q_vel_desired[1][i]-20*e[1]];
  vdot = [q_acc_desired[0][i]-20*edot[0],q_acc_desired[1][i]-20*edot[1]]
  a_ = vdot;
  r = np.array([q_vel[0][i]-v[0],q_vel[1][i]-v[1]]); 

  g = 9.8
  Y = np.zeros((2,5))
  Y[0,0] = a_[0]
  Y[0,1] = math.cos(q_pos[0][i])*(2*a_[0]+a_[1])-math.sin(q_pos[1][i]*v[0]+q_vel[0][i]*v[1]+q_vel[1][i]*v[1])
  Y[0,2] = a_[1]
  Y[0,3] = g*math.cos(q_pos[0][i])
  Y[0,4] = g*math.cos(q_pos[0][i]+q_pos[1][i])
  Y[1,0] = 0
  Y[1,1] = math.cos(q_pos[1][i]*a_[0])+math.sin(q_pos[1][i])*q_vel[0][i]*v[0]
  Y[1,2] = a_[0]+a_[1]
  Y[1,3] = 0
  Y[1,4] = g*math.cos(q_pos[0][i]+q_pos[1][i])
  Gamma = 2*np.eye(5)
  #print(Gamma.shape)
  #print(Y.shape)
  #print(np.matmul(Gamma,Y.T))
  theta_hat_dot = -np.matmul(np.matmul(np.linalg.inv(Gamma),np.transpose(Y)),r)

  theta_hat = theta_hat+ theta_hat_dot*steps
  
  K = 100*np.eye(2)
  u = np.matmul(Y,theta_hat)-np.matmul(K,r)
  #print(e)
  torque = bullet.calculateInverseDynamics(id_robot, obj_pos, obj_vel, obj_acc)
  torque = u
  q_tor[0][i] = torque[0]
  q_tor[1][i] = torque[1]
  if (verbose):
    print("torque=")
    print(torque)
  
  # Set the Joint Torques:
  bullet.setJointMotorControlArray(id_robot,
                                   id_revolute_joints,
                                   bullet.TORQUE_CONTROL,
                                   forces=[torque[0], torque[1]])

  # Step Simulation
  bullet.stepSimulation()

# Plot the Position, Velocity and Acceleration:
if plot:
  figure = plt.figure(figsize=[15, 4.5])
  figure.subplots_adjust(left=0.05, bottom=0.11, right=0.97, top=0.9, wspace=0.4, hspace=0.55)

  ax_pos = figure.add_subplot(141)
  ax_pos.set_title("Joint Position")
  ax_pos.plot(t, q_pos_desired[0], '--r', lw=4, label='Desired q0')
  ax_pos.plot(t, q_pos_desired[1], '--b', lw=4, label='Desired q1')
  ax_pos.plot(t, q_pos[0], '-r', lw=1, label='Measured q0')
  ax_pos.plot(t, q_pos[1], '-b', lw=1, label='Measured q1')
  ax_pos.set_ylim(-10., 10.)
  ax_pos.legend()

  ax_vel = figure.add_subplot(142)
  ax_vel.set_title("Joint Velocity")
  ax_vel.plot(t, q_vel_desired[0], '--r', lw=4, label='Desired q0')
  ax_vel.plot(t, q_vel_desired[1], '--b', lw=4, label='Desired q1')
  ax_vel.plot(t, q_vel[0], '-r', lw=1, label='Measured q0')
  ax_vel.plot(t, q_vel[1], '-b', lw=1, label='Measured q1')
  ax_vel.set_ylim(-2., 2.)
  ax_vel.legend()

  ax_acc = figure.add_subplot(143)
  ax_acc.set_title("Joint Acceleration")
  ax_acc.plot(t, q_acc_desired[0], '--r', lw=4, label='Desired q0')
  ax_acc.plot(t, q_acc_desired[1], '--b', lw=4, label='Desired q1')
  ax_acc.set_ylim(-10., 10.)
  ax_acc.legend()

  ax_tor = figure.add_subplot(144)
  ax_tor.set_title("Executed Torque")
  ax_tor.plot(t, q_tor[0], '-r', lw=2, label='Torque q0')
  ax_tor.plot(t, q_tor[1], '-b', lw=2, label='Torque q1')
  ax_tor.set_ylim(-20., 20.)
  ax_tor.legend()

  plt.pause(0.01)




K = 100*np.eye(2)
Lamda =20*np.eye(2)
Gamma = 2*np.eye(5)
theta_hat = np.array([0,0,0,0,0])
s_time = 0.001;
tf = 20;

q = np.transpose(np.array([0,0]))
qdot = np.transpose(np.array([0,0]))
qtwodot = np.transpose(np.array([0,0]))


while (1):


  bullet.stepSimulation()
  time.sleep(0.01)
