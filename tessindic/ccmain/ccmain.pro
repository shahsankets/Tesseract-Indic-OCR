######################################################################
# Automatically generated by qmake (2.01a) Tue Jun 29 08:36:47 2010
######################################################################
include(../ccutil/ccutil.pri)
include(../cutil/cutil.pri)
include(../ccstruct/ccstruct.pri)
include(../classify/classify.pri)
include(../dict/dict.pri)
include(../image/image.pri)
include(../wordrec/wordrec.pri)
include(../pageseg/pageseg.pri)
include(../viewer/viewer.pri)
include(../textord/textord.pri)

TEMPLATE = app
TARGET = tesseractArm
DEPENDPATH += . ../ccutil/ ../image/ ../classify/ ../wordrec/ ../textord/ ../ccstruct/ ../dict/ ../cutil/  ../pageseg ../viewer 
INCLUDEPATH += . ../ccutil/ ../image/ ../classify/ ../wordrec/ ../textord/ ../ccstruct/ ../dict/ ../cutil/ ../pageseg ../viewer
QMAKE_LIBDIR += /mnt/qt-arm/lib/ /home/debayan/symbian-sdk/epoc32/release/armv5/lib/
LIBS += libstdcpp
DEFINES += __UNIX__ __linux__ GRAPHICS_DISABLED

# Input
HEADERS += adaptions.h \
           applybox.h \
           baseapi.h \
           blobcmp.h \
           callnet.h \
           charcut.h \
           control.h \
           docqual.h \
           expandblob.h \
           fixspace.h \
           fixxht.h \
           imgscale.h \
           matmatch.h \
           output.h \
           pagewalk.h \
           paircmp.h \
           pgedit.h \
           reject.h \
           scaleimg.h \
           tessbox.h \
           tessedit.h \
           tesseractmain.h \
           tessio.h \
           tessvars.h \
           tfacep.h \
           tfacepp.h \
           tstruct.h \
           varabled.h \
           werdit.h
SOURCES += adaptions.cpp \
           applybox.cpp \
           baseapi.cpp \
           blobcmp.cpp \
           callnet.cpp \
           charcut.cpp \
           charsample.cpp \
           control.cpp \
           docqual.cpp \
           expandblob.cpp \
           fixspace.cpp \
           fixxht.cpp \
           imgscale.cpp \
           matmatch.cpp \
           output.cpp \
           pagewalk.cpp \
           paircmp.cpp \
           pgedit.cpp \
           reject.cpp \
           scaleimg.cpp \
           tessbox.cpp \
           tessedit.cpp \
           tesseractfull.cc \
           tesseractmain.cpp \
           tessvars.cpp \
           tfacepp.cpp \
           tstruct.cpp \
           varabled.cpp \
           werdit.cpp
# install
target.path = .
INSTALLS += target

symbian {
    TARGET.UID3 = 0xA000C610
    include(/home/debayan/code/qt-source-code/qt/examples/symbianpkgrules.pri)
}
