

import QtQuick 2.6
import QtQuick.Layouts 1.3
import QtQuick.Controls 2.1
import QtQuick.Controls.Material 2.1
import QtQuick.Dialogs 1.0

Item {
    id: mainView
    Material.theme: Material.Dark
    Material.accent: Material.Red

    anchors.fill: parent
    anchors.margins: 10

    // Rectangle
    // {
    //     id: background
    //     color: "white"
    //     anchors.fill: parent
    // }

    Flickable {
        id: flickableArea
        focus: true
        anchors.fill: parent
        anchors.margins: 10
        contentWidth: configPanel.width
        contentHeight: configPanel.height
        // contentY : 20
        boundsBehavior: Flickable.StopAtBounds        

        Keys.onUpPressed: verticalScrollBar.decrease()
        Keys.onDownPressed: verticalScrollBar.increase()

        ScrollBar.vertical: ScrollBar {
            id: verticalScrollBar
            Binding {
                target: verticalScrollBar
                property: "active"
                value: verticalScrollBar.hovered
            }
        }

        ColumnLayout {
            id: configPanel
            anchors.margins: 10
            width: mainView.width - 20
            CheckBox {
                id: is_auto_resolv
                checked: false
                text: qsTr("Поддерживает ли сервер автоматическое создание файла resolv.conf?")
            }
            CheckBox {
                id: is_dhcp
                checked: false
                text: qsTr("IP-адрес динамический и присваивается DHCP сервером?")
            }
            ColumnLayout {
                // Rectangle {
                //     anchors.fill: parent
                //     color: "red"
                // }
                RowLayout {
                    Label {
                        text: qsTr("Домен для входа:\t")
                    }
                    TextField {
                        id: domain
                        Layout.fillWidth: true
                        // validator: validator: RegExpValidator { regExp: /^((?!-))(xn--)?[a-z0-9][a-z0-9-_]{0,61}[a-z0-9]{0,1}\.(xn--)?([a-z0-9\-]{1,61}|[a-z0-9-]{1,30}\.[a-z]{2,})$/ }
                        // inputMethodHints: Qt.ImhNone
                        placeholderText: qsTr("example.com")
                        ToolTip {
                            x: 0
                            visible: parent.hovered
                            text: qsTr("Домен для входа. Пример: example.com")
                            delay: 1000
                        }

                    }
                }
                Repeater {
                    id: dns_list
                    model: 0
                    ColumnLayout {
                        RowLayout {
                            property string host: ""
                            property string ip: ""
                            property bool is_admin_server: false
                            Label {
                                text: qsTr("Имя DNS сервер:\t")
                            }
                            TextField {
                                Layout.fillWidth: true
                                text: parent.host
                                // validator: validator: RegExpValidator { regExp: /^((?!-))(xn--)?[a-z0-9][a-z0-9-_]{0,61}[a-z0-9]{0,1}\.(xn--)?([a-z0-9\-]{1,61}|[a-z0-9-]{1,30}\.[a-z]{2,})$/ }
                                // inputMethodHints: Qt.ImhNone
                                placeholderText: qsTr("dc")
                                ToolTip {
                                    x: 0
                                    visible: parent.hovered
                                    text: qsTr("Имя DNS сервер домена. Пример: dc")
                                    delay: 1000
                                }
                            }
                            // TextField {
                            //     color: "red"
                            //     Layout.fillWidth: true
                            //     text: parent.ip
                            //     // validator: RegExpValidator {
                            //     //     regExp:  /^\d{9}$/
                            //     // }
                            //     // validator: RegExpValidator { regExp: /^((?!-))(xn--)?[a-z0-9][a-z0-9-_]{0,61}[a-z0-9]{0,1}\.(xn--)?([a-z0-9\-]{1,61}|[a-z0-9-]{1,30}\.[a-z]{2,})$/ }
                            //     // inputMethodHints: Qt.ImhDigitsOnly
                            //     // inputMask: "000.000.000.000;_"
                            //     placeholderText: qsTr("192.168.0.1")
                            //     ToolTip {
                            //         x: 0
                            //         visible: parent.hovered
                            //         text: qsTr("Домен для входа. Пример: example.com")
                            //         delay: 1000
                            //     }
                            // }
                        }
                        RowLayout {
                            property string host: ""
                            property string ip: ""
                            property bool is_admin_server: false
                            Label {
                                text: qsTr("IP адрес DNS:\t")
                            }
                            TextField {
                                Layout.fillWidth: true
                                text: parent.ip
                                validator: RegExpValidator {
                                    regExp:  /^((?:[0-1]?[0-9]?[0-9]|2[0-4][0-9]|25[0-5])\.){0,3}(?:[0-1]?[0-9]?[0-9]|2[0-4][0-9]|25[0-5])$/
                                }
                                // validator: RegExpValidator { regExp: /^((?!-))(xn--)?[a-z0-9][a-z0-9-_]{0,61}[a-z0-9]{0,1}\.(xn--)?([a-z0-9\-]{1,61}|[a-z0-9-]{1,30}\.[a-z]{2,})$/ }
                                // inputMethodHints: Qt.ImhNone
                                placeholderText: qsTr("192.168.0.1")
                                ToolTip {
                                    x: 0
                                    visible: parent.hovered
                                    text: qsTr("IP адрес DNS сервера. Пример: 192.168.0.1")
                                    delay: 1000
                                }
                            }
                        }
                    }
                    // Rectangle {
                    //     width: 100; height: 40
                    //     border.width: 1
                    //     color: "yellow"
                    // }
                }
            }
            Button {
                text: "Добавить DNS сервер"
                onClicked: { 
                    ++dns_list.model
                    dns_list.itemAt(0)
                    PyConsole.log("test")
                }
            }
            RowLayout {
                Label {
                    text: qsTr("Имя компьютера:\t")
                }
                TextField {
                    id: hostname
                    Layout.fillWidth: true
                    // validator: validator: RegExpValidator { regExp: /^((?!-))(xn--)?[a-z0-9][a-z0-9-_]{0,61}[a-z0-9]{0,1}\.(xn--)?([a-z0-9\-]{1,61}|[a-z0-9-]{1,30}\.[a-z]{2,})$/ }
                    // inputMethodHints: Qt.ImhNone
                    placeholderText: qsTr("smbsrv01")
                    ToolTip {
                        x: 0
                        visible: parent.hovered
                        text: qsTr("HOSTNAME данного компьютера. Пример: smbsrv01")
                        delay: 1000
                    }

                }
            }
            RowLayout {
                Label {
                    text: qsTr("Сервер синхронизации:\t")
                }
                TextField {
                    id: time_server
                    Layout.fillWidth: true
                    // validator: validator: RegExpValidator { regExp: /^((?!-))(xn--)?[a-z0-9][a-z0-9-_]{0,61}[a-z0-9]{0,1}\.(xn--)?([a-z0-9\-]{1,61}|[a-z0-9-]{1,30}\.[a-z]{2,})$/ }
                    // inputMethodHints: Qt.ImhNone
                    placeholderText: qsTr("dc.domain.com")
                    ToolTip {
                        x: 0
                        visible: parent.hovered
                        text: qsTr("Сервер для автоматической синхронизации времени. Пример: dc.domain.com")
                        delay: 1000
                    }

                }
            }
            Button {
                text: qsTr("Применить настройки")
                width: parent.width
                onClicked: {
                    mainView.enabled = false
                    // filtersController.gaussianBlur(colorModelSelector.colorModelTag, colorModelSelector.currentImageChannelIndex, isOriginalImage.checked, filterWidth.text, filterHeight.text)
                    mainView.enabled = true
                    // mainView.updateProcessingImage()
                }
            }
        }
    }
}