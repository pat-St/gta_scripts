QT += qml quick

# You can make your code fail to compile if it uses deprecated APIs.
# In order to do so, uncomment the following line.
#DEFINES += QT_DISABLE_DEPRECATED_BEFORE=0x060000    # disables all the APIs deprecated before Qt 6.0.0

CONFIG += c++17 qmltypes static
QML_IMPORT_NAME = ScriptUI
QML_IMPORT_MAJOR_VERSION = 1

HEADERS += \
    jobList.h \
    jobmodel.h \
    processoutputlog.h \
    scriptHandler.h

SOURCES += \
        jobList.cpp \
        jobmodel.cpp \
        main.cpp \
        processoutputlog.cpp \
        scriptHandler.cpp

#resource.file = qml.qrc
#resource.prefix = ui/

RESOURCES += qml.qrc qtquickcontrols2.conf

# Additional import path used to resolve QML modules in Qt Creator's code model
#QML_IMPORT_PATH =

# Additional import path used to resolve QML modules just for Qt Quick Designer
#QML_DESIGNER_IMPORT_PATH =

# Default rules for deployment.
qnx: target.path = /tmp/$${TARGET}/bin
else: unix:!android: target.path = /opt/$${TARGET}/bin
!isEmpty(target.path): INSTALLS += target

