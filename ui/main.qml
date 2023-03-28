import QtQuick
import QtQuick.Controls
import QtQuick.Controls.Material
import QtQuick.Window
import QtQuick.Layouts
import Job

//import QtMultimedia
ApplicationWindow {
    width: 720
    height: 460
    visible: true
    title: qsTr("GTA RP Script")
//    Material.theme: Material.System

    Component {
        id: jobModelView
        Item {
            id: item
            required property string name
            required property bool isActive
            required property int index
            width: jobcell.cellWidth
            height: jobcell.cellHeight
            Row {
                anchors.fill: parent
                spacing: 15

                Button {
                    id: startButton
                    width: 70
                    text: if (isActive === false)
                              qsTr("Start")
                          else
                              qsTr("Stop")
                    Material.accent: Material.Orange
                    onClicked: jobList.changeState(name)
                }
                Pane {
                    Layout.fillWidth: true
                    width: jobcell.cellWidth*0.5
                    Text {
                        Layout.preferredWidth: jobcell.cellWidth*0.5
                        text: qsTr(name)
                    }
                }
                BusyIndicator {
                    width: 50
                    running: isActive === true
                }
            }
        }
    }

    menuBar: TabBar {
        id: bar
        width: parent.width
        TabButton {
            text: qsTr("Jobs")
        }
        TabButton {
            text: qsTr("Actions")
        }
        TabButton {
            text: qsTr("Settings")
        }
    }

    StackLayout {
        id: stack
        anchors.fill: parent
        currentIndex: bar.currentIndex
        Item {
            id: jobsTab
            Layout.alignment: Qt.AlignJustify
            RowLayout {
                anchors.fill: parent
                GridView {
                    id: jobcell
                    Layout.alignment: Qt.AlignLeft | Qt.AlignTop
                    Layout.preferredHeight: parent.height //Math.abs(parent.height - 50)
                    Layout.preferredWidth: parent.width*0.5 //Math.min(parent.width, 700)
                    cellWidth: parent.width*0.4 //Math.min(parent.width, 700)
                    cellHeight: 50
                    model: JobModel {
                        list: jobList
                    }
                    delegate: jobModelView
                    focus: true
                }

                GridView {
                    id: processCell
                    Layout.alignment: Qt.AlignRight | Qt.AlignTop
                    Layout.fillWidth: true
                    Layout.preferredHeight: parent.height
                    Layout.preferredWidth: parent.width*0.5
                    cellWidth: parent.width*0.4
                    cellHeight: 50
                    model: ProcessOutputLog {
                        sh: scriptHandler
                    }

                    delegate: Row {
                        id: processOutputLogObj
//                        anchors.fill: parent
//                        spacing: 15
                            Text {
                                width: processCell.width //300
                                Layout.alignment: Qt.AlignCenter | Qt.AlignVCenter
                                text: qsTr(output)
                            }
                    }
                    focus: true
                }
                //                Pane {
                //                    Layout.fillHeight: true

                //                    Layout.preferredWidth: parent.width * 0.6
                //                    Layout.alignment: Qt.AlignRight
                //                    width: 300
                //                    height: 400
                //                    Rectangle {
                //                        color: "red"
                //                        Layout.preferredWidth: 300
                //                        Layout.preferredHeight: 400
                //                        //
                //                    }
                //                }

                //                Pane {
                //                    Layout.fillHeight: true

                //                    Layout.preferredWidth: parent.width * 0.6
                //                    Layout.alignment: Qt.AlignRight
                //                    RoundButton {
                //                        anchors.centerIn: parent
                //                        width: 100
                //                        height: 100
                //                        text: qsTr("|>")
                //                        visible: mediaplayer.playbackState == 0
                //                    }

                //                    MediaPlayer {
                //                        id: mediaplayer
                //                        source: "file:///home/patrick/repo/git/gta_scripts/assets/fischen_ges.mp4"
                //                        audioOutput: AudioOutput {}
                //                        videoOutput: videoOutput
                //                    }
                //                    VideoOutput {
                //                        id: videoOutput
                //                        anchors.fill: parent
                //                    }

                //                    MouseArea {
                //                        anchors.fill: parent
                //                        onPressed: if (mediaplayer.playbackState == 0)
                //                                       mediaplayer.play()
                //                                   else
                //                                       mediaplayer.stop()
                //                    }
                //                }
            }
        }
    }
    Item {
        id: actionsTab
        anchors.fill: parent
    }
    Item {
        id: settingsTab
        anchors.fill: parent
    }
}
