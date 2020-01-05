# CMake generated Testfile for 
# Source directory: /home/sung/bullet3/data/cmake-3.15.3
# Build directory: /home/sung/bullet3/data/cmake-3.15.3
# 
# This file includes the relevant testing commands required for 
# testing this directory and lists subdirectories to be tested as well.
include("/home/sung/bullet3/data/cmake-3.15.3/Tests/EnforceConfig.cmake")
add_test(SystemInformationNew "/home/sung/bullet3/data/cmake-3.15.3/bin/cmake" "--system-information" "-G" "Unix Makefiles")
set_tests_properties(SystemInformationNew PROPERTIES  _BACKTRACE_TRIPLES "/home/sung/bullet3/data/cmake-3.15.3/CMakeLists.txt;801;add_test;/home/sung/bullet3/data/cmake-3.15.3/CMakeLists.txt;0;")
subdirs("Source/kwsys")
subdirs("Utilities/KWIML")
subdirs("Utilities/cmlibrhash")
subdirs("Utilities/cmzlib")
subdirs("Utilities/cmcurl")
subdirs("Utilities/cmexpat")
subdirs("Utilities/cmbzip2")
subdirs("Utilities/cmzstd")
subdirs("Utilities/cmliblzma")
subdirs("Utilities/cmlibarchive")
subdirs("Utilities/cmjsoncpp")
subdirs("Utilities/cmlibuv")
subdirs("Source")
subdirs("Utilities")
subdirs("Tests")
subdirs("Auxiliary")
