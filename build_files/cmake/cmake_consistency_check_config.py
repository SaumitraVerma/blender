import os

IGNORE = (
    "/test/",
    "/tests/gtests/",
    "/BSP_GhostTest/",
    "/release/",
    "/xembed/",
    "/TerraplayNetwork/",
    "/ik_glut_test/",

    # specific source files
    "extern/bullet2/src/BulletCollision/CollisionDispatch/btBox2dBox2dCollisionAlgorithm.cpp",
    "extern/bullet2/src/BulletCollision/CollisionDispatch/btConvex2dConvex2dAlgorithm.cpp",
    "extern/bullet2/src/BulletCollision/CollisionDispatch/btInternalEdgeUtility.cpp",
    "extern/bullet2/src/BulletCollision/CollisionShapes/btBox2dShape.cpp",
    "extern/bullet2/src/BulletCollision/CollisionShapes/btConvex2dShape.cpp",
    "extern/bullet2/src/BulletDynamics/Character/btKinematicCharacterController.cpp",
    "extern/bullet2/src/BulletDynamics/ConstraintSolver/btHinge2Constraint.cpp",
    "extern/bullet2/src/BulletDynamics/ConstraintSolver/btUniversalConstraint.cpp",
    "extern/eltopo/common/meshes/ObjLoader.cpp",
    "extern/eltopo/common/meshes/meshloader.cpp",
    "extern/eltopo/common/openglutils.cpp",
    "extern/eltopo/eltopo3d/broadphase_blenderbvh.cpp",
    "source/blender/imbuf/intern/imbuf_cocoa.m",
    "extern/recastnavigation/Recast/Source/RecastLog.cpp",
    "extern/recastnavigation/Recast/Source/RecastTimer.cpp",
    "intern/audaspace/SRC/AUD_SRCResampleFactory.cpp",
    "intern/audaspace/SRC/AUD_SRCResampleReader.cpp",
    "intern/cycles/render/film_response.cpp",
    "extern/libmv/third_party/ceres/internal/ceres/generated/schur_eliminator_2_2_2.cc",
    "extern/libmv/third_party/ceres/internal/ceres/generated/schur_eliminator_2_2_3.cc",
    "extern/libmv/third_party/ceres/internal/ceres/generated/schur_eliminator_2_2_4.cc",
    "extern/libmv/third_party/ceres/internal/ceres/generated/schur_eliminator_2_2_d.cc",
    "extern/libmv/third_party/ceres/internal/ceres/generated/schur_eliminator_2_3_3.cc",
    "extern/libmv/third_party/ceres/internal/ceres/generated/schur_eliminator_2_3_4.cc",
    "extern/libmv/third_party/ceres/internal/ceres/generated/schur_eliminator_2_3_9.cc",
    "extern/libmv/third_party/ceres/internal/ceres/generated/schur_eliminator_2_3_d.cc",
    "extern/libmv/third_party/ceres/internal/ceres/generated/schur_eliminator_2_4_3.cc",
    "extern/libmv/third_party/ceres/internal/ceres/generated/schur_eliminator_2_4_4.cc",
    "extern/libmv/third_party/ceres/internal/ceres/generated/schur_eliminator_2_4_d.cc",
    "extern/libmv/third_party/ceres/internal/ceres/generated/schur_eliminator_4_4_2.cc",
    "extern/libmv/third_party/ceres/internal/ceres/generated/schur_eliminator_4_4_3.cc",
    "extern/libmv/third_party/ceres/internal/ceres/generated/schur_eliminator_4_4_4.cc",
    "extern/libmv/third_party/ceres/internal/ceres/generated/schur_eliminator_4_4_d.cc",

    "extern/bullet2/src/BulletCollision/CollisionDispatch/btBox2dBox2dCollisionAlgorithm.h",
    "extern/bullet2/src/BulletCollision/CollisionDispatch/btConvex2dConvex2dAlgorithm.h",
    "extern/bullet2/src/BulletCollision/CollisionDispatch/btInternalEdgeUtility.h",
    "extern/bullet2/src/BulletCollision/CollisionShapes/btBox2dShape.h",
    "extern/bullet2/src/BulletCollision/CollisionShapes/btConvex2dShape.h",
    "extern/bullet2/src/BulletDynamics/Character/btKinematicCharacterController.h",
    "extern/bullet2/src/BulletDynamics/ConstraintSolver/btHinge2Constraint.h",
    "extern/bullet2/src/BulletDynamics/ConstraintSolver/btUniversalConstraint.h",
    "extern/eltopo/common/meshes/Edge.hpp",
    "extern/eltopo/common/meshes/ObjLoader.hpp",
    "extern/eltopo/common/meshes/TriangleIndex.hpp",
    "extern/eltopo/common/meshes/meshloader.h",
    "extern/eltopo/eltopo3d/broadphase_blenderbvh.h",
    "extern/recastnavigation/Recast/Include/RecastLog.h",
    "extern/recastnavigation/Recast/Include/RecastTimer.h",
    "intern/audaspace/SRC/AUD_SRCResampleFactory.h",
    "intern/audaspace/SRC/AUD_SRCResampleReader.h",
    "intern/cycles/render/film_response.h",
    "extern/carve/include/carve/config.h",
    "extern/carve/include/carve/external/boost/random.hpp",
    "extern/carve/patches/files/config.h",
    "extern/carve/patches/files/random.hpp",
    "extern/cuew/auto/stdlib.h",
    )

UTF8_CHECK = True

SOURCE_DIR = os.path.normpath(os.path.abspath(os.path.normpath(os.path.join(os.path.dirname(__file__), "..", ".."))))

# doesn't have to exist, just use as reference
BUILD_DIR = os.path.normpath(os.path.abspath(os.path.normpath(os.path.join(SOURCE_DIR, "..", "build"))))
