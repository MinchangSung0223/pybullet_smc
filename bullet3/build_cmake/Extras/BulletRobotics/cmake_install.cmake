# Install script for directory: /home/sung/workspace/bullet/bullet3/Extras/BulletRobotics

# Set the install prefix
if(NOT DEFINED CMAKE_INSTALL_PREFIX)
  set(CMAKE_INSTALL_PREFIX "/usr/local")
endif()
string(REGEX REPLACE "/$" "" CMAKE_INSTALL_PREFIX "${CMAKE_INSTALL_PREFIX}")

# Set the install configuration name.
if(NOT DEFINED CMAKE_INSTALL_CONFIG_NAME)
  if(BUILD_TYPE)
    string(REGEX REPLACE "^[^A-Za-z0-9_]+" ""
           CMAKE_INSTALL_CONFIG_NAME "${BUILD_TYPE}")
  else()
    set(CMAKE_INSTALL_CONFIG_NAME "Release")
  endif()
  message(STATUS "Install configuration: \"${CMAKE_INSTALL_CONFIG_NAME}\"")
endif()

# Set the component getting installed.
if(NOT CMAKE_INSTALL_COMPONENT)
  if(COMPONENT)
    message(STATUS "Install component: \"${COMPONENT}\"")
    set(CMAKE_INSTALL_COMPONENT "${COMPONENT}")
  else()
    set(CMAKE_INSTALL_COMPONENT)
  endif()
endif()

# Install shared libraries without execute permission?
if(NOT DEFINED CMAKE_INSTALL_SO_NO_EXE)
  set(CMAKE_INSTALL_SO_NO_EXE "1")
endif()

# Is this installation the result of a crosscompile?
if(NOT DEFINED CMAKE_CROSSCOMPILING)
  set(CMAKE_CROSSCOMPILING "FALSE")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/include/bullet" TYPE FILE FILES
    "/home/sung/workspace/bullet/bullet3/Extras/BulletRobotics/../../examples/SharedMemory/PhysicsClientC_API.h"
    "/home/sung/workspace/bullet/bullet3/Extras/BulletRobotics/../../examples/SharedMemory/PhysicsClientSharedMemory_C_API.h"
    "/home/sung/workspace/bullet/bullet3/Extras/BulletRobotics/../../examples/SharedMemory/PhysicsClientSharedMemory2_C_API.h"
    "/home/sung/workspace/bullet/bullet3/Extras/BulletRobotics/../../examples/SharedMemory/PhysicsDirectC_API.h"
    "/home/sung/workspace/bullet/bullet3/Extras/BulletRobotics/../../examples/SharedMemory/PhysicsClientUDP_C_API.h"
    "/home/sung/workspace/bullet/bullet3/Extras/BulletRobotics/../../examples/SharedMemory/PhysicsClientTCP_C_API.h"
    "/home/sung/workspace/bullet/bullet3/Extras/BulletRobotics/../../examples/SharedMemory/SharedMemoryInProcessPhysicsC_API.h"
    "/home/sung/workspace/bullet/bullet3/Extras/BulletRobotics/../../examples/SharedMemory/SharedMemoryPublic.h"
    "/home/sung/workspace/bullet/bullet3/Extras/BulletRobotics/../../examples/SharedMemory/b3RobotSimulatorClientAPI_NoGUI.h"
    "/home/sung/workspace/bullet/bullet3/Extras/BulletRobotics/../../examples/SharedMemory/b3RobotSimulatorClientAPI_NoDirect.h"
    )
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/include/bullet_robotics" TYPE FILE FILES
    "/home/sung/workspace/bullet/bullet3/Extras/BulletRobotics/../../examples/CommonInterfaces/Common2dCanvasInterface.h"
    "/home/sung/workspace/bullet/bullet3/Extras/BulletRobotics/../../examples/CommonInterfaces/CommonCallbacks.h"
    "/home/sung/workspace/bullet/bullet3/Extras/BulletRobotics/../../examples/CommonInterfaces/CommonCameraInterface.h"
    "/home/sung/workspace/bullet/bullet3/Extras/BulletRobotics/../../examples/CommonInterfaces/CommonExampleInterface.h"
    "/home/sung/workspace/bullet/bullet3/Extras/BulletRobotics/../../examples/CommonInterfaces/CommonFileIOInterface.h"
    "/home/sung/workspace/bullet/bullet3/Extras/BulletRobotics/../../examples/CommonInterfaces/CommonGraphicsAppInterface.h"
    "/home/sung/workspace/bullet/bullet3/Extras/BulletRobotics/../../examples/CommonInterfaces/CommonGUIHelperInterface.h"
    "/home/sung/workspace/bullet/bullet3/Extras/BulletRobotics/../../examples/CommonInterfaces/CommonMultiBodyBase.h"
    "/home/sung/workspace/bullet/bullet3/Extras/BulletRobotics/../../examples/CommonInterfaces/CommonParameterInterface.h"
    "/home/sung/workspace/bullet/bullet3/Extras/BulletRobotics/../../examples/CommonInterfaces/CommonRenderInterface.h"
    "/home/sung/workspace/bullet/bullet3/Extras/BulletRobotics/../../examples/CommonInterfaces/CommonRigidBodyBase.h"
    "/home/sung/workspace/bullet/bullet3/Extras/BulletRobotics/../../examples/CommonInterfaces/CommonWindowInterface.h"
    "/home/sung/workspace/bullet/bullet3/Extras/BulletRobotics/../../examples/OpenGLWindow/SimpleCamera.h"
    "/home/sung/workspace/bullet/bullet3/Extras/BulletRobotics/../../examples/TinyRenderer/geometry.h"
    "/home/sung/workspace/bullet/bullet3/Extras/BulletRobotics/../../examples/TinyRenderer/model.h"
    "/home/sung/workspace/bullet/bullet3/Extras/BulletRobotics/../../examples/TinyRenderer/tgaimage.h"
    "/home/sung/workspace/bullet/bullet3/Extras/BulletRobotics/../../examples/TinyRenderer/our_gl.h"
    "/home/sung/workspace/bullet/bullet3/Extras/BulletRobotics/../../examples/TinyRenderer/TinyRenderer.h"
    "/home/sung/workspace/bullet/bullet3/Extras/BulletRobotics/../../examples/SharedMemory/plugins/collisionFilterPlugin/collisionFilterPlugin.h"
    "/home/sung/workspace/bullet/bullet3/Extras/BulletRobotics/../../examples/SharedMemory/plugins/pdControlPlugin/pdControlPlugin.h"
    "/home/sung/workspace/bullet/bullet3/Extras/BulletRobotics/../../examples/SharedMemory/b3RobotSimulatorClientAPI_NoGUI.h"
    "/home/sung/workspace/bullet/bullet3/Extras/BulletRobotics/../../examples/SharedMemory/b3RobotSimulatorClientAPI_NoDirect.h"
    "/home/sung/workspace/bullet/bullet3/Extras/BulletRobotics/../../examples/SharedMemory/IKTrajectoryHelper.h"
    "/home/sung/workspace/bullet/bullet3/Extras/BulletRobotics/../../examples/SharedMemory/plugins/tinyRendererPlugin/tinyRendererPlugin.h"
    "/home/sung/workspace/bullet/bullet3/Extras/BulletRobotics/../../examples/SharedMemory/plugins/tinyRendererPlugin/TinyRendererVisualShapeConverter.h"
    "/home/sung/workspace/bullet/bullet3/Extras/BulletRobotics/../../examples/SharedMemory/InProcessMemory.h"
    "/home/sung/workspace/bullet/bullet3/Extras/BulletRobotics/../../examples/SharedMemory/PhysicsServer.h"
    "/home/sung/workspace/bullet/bullet3/Extras/BulletRobotics/../../examples/SharedMemory/PhysicsClient.h"
    "/home/sung/workspace/bullet/bullet3/Extras/BulletRobotics/../../examples/SharedMemory/PhysicsServerSharedMemory.h"
    "/home/sung/workspace/bullet/bullet3/Extras/BulletRobotics/../../examples/SharedMemory/PhysicsDirect.h"
    "/home/sung/workspace/bullet/bullet3/Extras/BulletRobotics/../../examples/SharedMemory/PhysicsDirectC_API.h"
    "/home/sung/workspace/bullet/bullet3/Extras/BulletRobotics/../../examples/SharedMemory/PhysicsServerCommandProcessor.h"
    "/home/sung/workspace/bullet/bullet3/Extras/BulletRobotics/../../examples/SharedMemory/b3PluginManager.h"
    "/home/sung/workspace/bullet/bullet3/Extras/BulletRobotics/../../examples/SharedMemory/PhysicsClientSharedMemory.h"
    "/home/sung/workspace/bullet/bullet3/Extras/BulletRobotics/../../examples/SharedMemory/PhysicsClientSharedMemory_C_API.h"
    "/home/sung/workspace/bullet/bullet3/Extras/BulletRobotics/../../examples/SharedMemory/PhysicsClientC_API.h"
    "/home/sung/workspace/bullet/bullet3/Extras/BulletRobotics/../../examples/SharedMemory/SharedMemoryPublic.h"
    "/home/sung/workspace/bullet/bullet3/Extras/BulletRobotics/../../examples/SharedMemory/Win32SharedMemory.h"
    "/home/sung/workspace/bullet/bullet3/Extras/BulletRobotics/../../examples/SharedMemory/PosixSharedMemory.h"
    "/home/sung/workspace/bullet/bullet3/Extras/BulletRobotics/../../examples/Utils/b3ResourcePath.h"
    "/home/sung/workspace/bullet/bullet3/Extras/BulletRobotics/../../examples/Utils/RobotLoggingUtil.h"
    "/home/sung/workspace/bullet/bullet3/Extras/BulletRobotics/../../examples/Utils/b3Clock.h"
    "/home/sung/workspace/bullet/bullet3/Extras/BulletRobotics/../../examples/Utils/b3ResourcePath.h"
    "/home/sung/workspace/bullet/bullet3/Extras/BulletRobotics/../../examples/Utils/ChromeTraceUtil.h"
    "/home/sung/workspace/bullet/bullet3/Extras/BulletRobotics/../../examples/Utils/b3ERPCFMHelper.hpp"
    "/home/sung/workspace/bullet/bullet3/Extras/BulletRobotics/../../examples/Utils/b3ReferenceFrameHelper.hpp"
    "/home/sung/workspace/bullet/bullet3/Extras/BulletRobotics/../../examples/ThirdPartyLibs/tinyxml2/tinyxml2.h"
    "/home/sung/workspace/bullet/bullet3/Extras/BulletRobotics/../../examples/ThirdPartyLibs/Wavefront/tiny_obj_loader.h"
    "/home/sung/workspace/bullet/bullet3/Extras/BulletRobotics/../../examples/ThirdPartyLibs/stb_image/stb_image.h"
    "/home/sung/workspace/bullet/bullet3/Extras/BulletRobotics/../../examples/ThirdPartyLibs/BussIK/Jacobian.h"
    "/home/sung/workspace/bullet/bullet3/Extras/BulletRobotics/../../examples/ThirdPartyLibs/BussIK/LinearR2.h"
    "/home/sung/workspace/bullet/bullet3/Extras/BulletRobotics/../../examples/ThirdPartyLibs/BussIK/LinearR3.h"
    "/home/sung/workspace/bullet/bullet3/Extras/BulletRobotics/../../examples/ThirdPartyLibs/BussIK/LinearR4.h"
    "/home/sung/workspace/bullet/bullet3/Extras/BulletRobotics/../../examples/ThirdPartyLibs/BussIK/MatrixRmn.h"
    "/home/sung/workspace/bullet/bullet3/Extras/BulletRobotics/../../examples/ThirdPartyLibs/BussIK/Node.h"
    "/home/sung/workspace/bullet/bullet3/Extras/BulletRobotics/../../examples/ThirdPartyLibs/BussIK/Tree.h"
    "/home/sung/workspace/bullet/bullet3/Extras/BulletRobotics/../../examples/ThirdPartyLibs/BussIK/VectorRn.h"
    "/home/sung/workspace/bullet/bullet3/Extras/BulletRobotics/../../examples/Importers/ImportColladaDemo/LoadMeshFromCollada.h"
    "/home/sung/workspace/bullet/bullet3/Extras/BulletRobotics/../../examples/Importers/ImportObjDemo/LoadMeshFromObj.h"
    "/home/sung/workspace/bullet/bullet3/Extras/BulletRobotics/../../examples/Importers/ImportObjDemo/Wavefront2GLInstanceGraphicsShape.h"
    "/home/sung/workspace/bullet/bullet3/Extras/BulletRobotics/../../examples/Importers/ImportMJCFDemo/BulletMJCFImporter.h"
    "/home/sung/workspace/bullet/bullet3/Extras/BulletRobotics/../../examples/Importers/ImportURDFDemo/BulletUrdfImporter.h"
    "/home/sung/workspace/bullet/bullet3/Extras/BulletRobotics/../../examples/Importers/ImportURDFDemo/MyMultiBodyCreator.h"
    "/home/sung/workspace/bullet/bullet3/Extras/BulletRobotics/../../examples/Importers/ImportURDFDemo/URDF2Bullet.h"
    "/home/sung/workspace/bullet/bullet3/Extras/BulletRobotics/../../examples/Importers/ImportURDFDemo/UrdfParser.h"
    "/home/sung/workspace/bullet/bullet3/Extras/BulletRobotics/../../examples/Importers/ImportURDFDemo/urdfStringSplit.h"
    "/home/sung/workspace/bullet/bullet3/Extras/BulletRobotics/../../examples/Importers/ImportURDFDemo/URDFImporterInterface.h"
    "/home/sung/workspace/bullet/bullet3/Extras/BulletRobotics/../../examples/Importers/ImportURDFDemo/URDFJointTypes.h"
    "/home/sung/workspace/bullet/bullet3/Extras/BulletRobotics/../../examples/Importers/ImportURDFDemo/SDFAudioTypes.h"
    "/home/sung/workspace/bullet/bullet3/Extras/BulletRobotics/../../examples/Importers/ImportURDFDemo/UrdfRenderingInterface.h"
    "/home/sung/workspace/bullet/bullet3/Extras/BulletRobotics/../../examples/Importers/ImportURDFDemo/MultiBodyCreationInterface.h"
    "/home/sung/workspace/bullet/bullet3/Extras/BulletRobotics/../../examples/Importers/ImportMeshUtility/b3ImportMeshUtility.h"
    "/home/sung/workspace/bullet/bullet3/Extras/BulletRobotics/../../examples/MultiThreading/b3PosixThreadSupport.h"
    "/home/sung/workspace/bullet/bullet3/Extras/BulletRobotics/../../examples/MultiThreading/b3Win32ThreadSupport.h"
    "/home/sung/workspace/bullet/bullet3/Extras/BulletRobotics/../../examples/MultiThreading/b3ThreadSupportInterface.h"
    "/home/sung/workspace/bullet/bullet3/Extras/BulletRobotics/../../examples/SharedMemory/PhysicsClientUDP.h"
    "/home/sung/workspace/bullet/bullet3/Extras/BulletRobotics/../../examples/SharedMemory/PhysicsClientUDP_C_API.h"
    "/home/sung/workspace/bullet/bullet3/Extras/BulletRobotics/../../examples/ThirdPartyLibs/enet/include/enet/win32.h"
    "/home/sung/workspace/bullet/bullet3/Extras/BulletRobotics/../../examples/ThirdPartyLibs/enet/include/enet/unix.h"
    "/home/sung/workspace/bullet/bullet3/Extras/BulletRobotics/../../examples/ThirdPartyLibs/enet/include/enet/callbacks.h"
    "/home/sung/workspace/bullet/bullet3/Extras/BulletRobotics/../../examples/ThirdPartyLibs/enet/include/enet/list.h"
    "/home/sung/workspace/bullet/bullet3/Extras/BulletRobotics/../../examples/ThirdPartyLibs/enet/include/enet/protocol.h"
    "/home/sung/workspace/bullet/bullet3/Extras/BulletRobotics/../../examples/SharedMemory/PhysicsClientTCP.h"
    "/home/sung/workspace/bullet/bullet3/Extras/BulletRobotics/../../examples/SharedMemory/PhysicsClientTCP_C_API.h"
    "/home/sung/workspace/bullet/bullet3/Extras/BulletRobotics/../../examples/ThirdPartyLibs/clsocket/src/SimpleSocket.h"
    "/home/sung/workspace/bullet/bullet3/Extras/BulletRobotics/../../examples/ThirdPartyLibs/clsocket/src/ActiveSocket.h"
    "/home/sung/workspace/bullet/bullet3/Extras/BulletRobotics/../../examples/ThirdPartyLibs/clsocket/src/PassiveSocket.h"
    )
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  if(EXISTS "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libBulletRobotics.so.2.89" AND
     NOT IS_SYMLINK "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libBulletRobotics.so.2.89")
    file(RPATH_CHECK
         FILE "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libBulletRobotics.so.2.89"
         RPATH "")
  endif()
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib" TYPE SHARED_LIBRARY FILES "/home/sung/workspace/bullet/bullet3/build_cmake/Extras/BulletRobotics/libBulletRobotics.so.2.89")
  if(EXISTS "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libBulletRobotics.so.2.89" AND
     NOT IS_SYMLINK "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libBulletRobotics.so.2.89")
    file(RPATH_CHANGE
         FILE "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libBulletRobotics.so.2.89"
         OLD_RPATH "/home/sung/workspace/bullet/bullet3/build_cmake/Extras/InverseDynamics:/home/sung/workspace/bullet/bullet3/build_cmake/Extras/Serialize/BulletWorldImporter:/home/sung/workspace/bullet/bullet3/build_cmake/Extras/Serialize/BulletFileLoader:/home/sung/workspace/bullet/bullet3/build_cmake/src/BulletSoftBody:/home/sung/workspace/bullet/bullet3/build_cmake/src/BulletDynamics:/home/sung/workspace/bullet/bullet3/build_cmake/src/BulletCollision:/home/sung/workspace/bullet/bullet3/build_cmake/src/BulletInverseDynamics:/home/sung/workspace/bullet/bullet3/build_cmake/src/LinearMath:/home/sung/workspace/bullet/bullet3/build_cmake/src/Bullet3Common:"
         NEW_RPATH "")
    if(CMAKE_INSTALL_DO_STRIP)
      execute_process(COMMAND "/usr/bin/strip" "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libBulletRobotics.so.2.89")
    endif()
  endif()
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  if(EXISTS "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libBulletRobotics.so" AND
     NOT IS_SYMLINK "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libBulletRobotics.so")
    file(RPATH_CHECK
         FILE "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libBulletRobotics.so"
         RPATH "")
  endif()
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib" TYPE SHARED_LIBRARY FILES "/home/sung/workspace/bullet/bullet3/build_cmake/Extras/BulletRobotics/libBulletRobotics.so")
  if(EXISTS "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libBulletRobotics.so" AND
     NOT IS_SYMLINK "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libBulletRobotics.so")
    file(RPATH_CHANGE
         FILE "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libBulletRobotics.so"
         OLD_RPATH "/home/sung/workspace/bullet/bullet3/build_cmake/Extras/InverseDynamics:/home/sung/workspace/bullet/bullet3/build_cmake/Extras/Serialize/BulletWorldImporter:/home/sung/workspace/bullet/bullet3/build_cmake/Extras/Serialize/BulletFileLoader:/home/sung/workspace/bullet/bullet3/build_cmake/src/BulletSoftBody:/home/sung/workspace/bullet/bullet3/build_cmake/src/BulletDynamics:/home/sung/workspace/bullet/bullet3/build_cmake/src/BulletCollision:/home/sung/workspace/bullet/bullet3/build_cmake/src/BulletInverseDynamics:/home/sung/workspace/bullet/bullet3/build_cmake/src/LinearMath:/home/sung/workspace/bullet/bullet3/build_cmake/src/Bullet3Common:"
         NEW_RPATH "")
    if(CMAKE_INSTALL_DO_STRIP)
      execute_process(COMMAND "/usr/bin/strip" "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libBulletRobotics.so")
    endif()
  endif()
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/pkgconfig" TYPE FILE FILES "/home/sung/workspace/bullet/bullet3/build_cmake/Extras/BulletRobotics/bullet_robotics.pc")
endif()

