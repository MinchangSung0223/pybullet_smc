import pybullet as p
import time

p.connect(p.GUI)
p.loadURDF("table/table.urdf", 0.5000000, 0.00000, -.820000, 0.000000, 0.000000, 0.0, 1.0)
p.setGravity(0, 0, -10)
arm = p.loadURDF("widowx/widowx.urdf", useFixedBase=True)

p.resetBasePositionAndOrientation(arm, [-0.098612, -0.000726, -0.194018],
                                  [0.000000, 0.000000, 0.000000, 1.000000])
shift = [0, -0.02, 0]
meshScale = [0.01, 0.01, 0.01]
#the visual shape and collision shape can be re-used by all createMultiBody instances (instancing)
visualShapeId = p.createVisualShape(shapeType=p.GEOM_MESH,
                                    fileName="object_1.obj",
                                    rgbaColor=[1, 1, 1, 1],
                                    specularColor=[0.4, .4, 0],
                                    visualFramePosition=shift,
                                    meshScale=meshScale)
collisionShapeId = p.createCollisionShape(shapeType=p.GEOM_MESH,
                                          fileName="object_1.obj",
                                          collisionFramePosition=shift,
                                       meshScale=meshScale)
rangex = 1
rangey = 1
for i in range(rangex):
  for j in range(rangey):
    p.createMultiBody(baseMass=1,
                      baseInertialFramePosition=[0, 0, 0],
                      baseCollisionShapeIndex=collisionShapeId,
                      baseVisualShapeIndex=visualShapeId,
                      basePosition=[((-rangex / 2) + i) * meshScale[0] * 2,
                                    (-rangey / 2 + j) * meshScale[1] * 2, 1],
                      useMaximalCoordinates=True)   
p.setRealTimeSimulation(1)
while (1):
  p.stepSimulation()
  time.sleep(0.001)
  #p.saveWorld("test.py")
  viewMat = p.getDebugVisualizerCamera()[2]
  #projMatrix = [0.7499999403953552, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, -1.0000200271606445, -1.0, 0.0, 0.0, -0.02000020071864128, 0.0]
  projMatrix = p.getDebugVisualizerCamera()[3]
  width = 640
  height = 480
  img_arr = p.getCameraImage(width=width,
                             height=height,
                             viewMatrix=viewMat,
                             projectionMatrix=projMatrix)
