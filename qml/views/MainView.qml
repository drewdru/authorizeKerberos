

import QtQuick 2.6
import QtQuick.Layouts 1.3
import QtQuick.Controls 2.1
import QtQuick.Controls.Material 2.1
import QtQuick.Dialogs 1.1
import "../js/mainView.js" as MVjs

Item {
    id: mainView
    Material.theme: Material.Dark
    Material.accent: Material.Red

    anchors.fill: parent
    anchors.margins: 10

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
                    Rectangle {
                        id: domainError
                        anchors.fill: parent
                        color: "#00FF0055"
                        visible: true
                    }
                }
                ButtonGroup { id: radioGroup }
                Repeater {
                    id: dns_list
                    model: ListModel {
                        id: modelTest;
                    }
                    delegate: ColumnLayout {
                        property string host: ""
                        property string ip: ""
                        property bool is_admin_server: false
                        RowLayout {
                            Label {
                                text: qsTr("Имя DNS сервера:\t")
                            }
                            TextField {
                                Layout.fillWidth: true
                                text: model.host
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
                            Rectangle {
                                // id: modelHostError
                                anchors.fill: parent
                                color: "#00FF0055"
                                visible: true
                            }
                        }
                        RowLayout {
                            Label {
                                text: qsTr("IP адрес DNS:\t")
                            }
                            TextField {
                                Layout.fillWidth: true
                                text: model.ip
                                validator: RegExpValidator {
                                    regExp:  /^((?:[0-1]?[0-9]?[0-9]|2[0-4][0-9]|25[0-5])\.){0,3}(?:[0-1]?[0-9]?[0-9]|2[0-4][0-9]|25[0-5])$/
                                }
                                // validator: RegExpValidator { regExp: /^((?!-))(xn--)?[a-z0-9][a-z0-9-_]{0,61}[a-z0-9]{0,1}\.(xn--)?([a-z0-9\-]{1,61}|[a-z0-9-]{1,30}\.[a-z]{2,})$/ }
                                // inputMethodHints: Qt.ImhNone
                                // inputMask: "000.000.000;"
                                placeholderText: qsTr("192.168.0.1")
                                ToolTip {
                                    x: 0
                                    visible: parent.hovered
                                    text: qsTr("IP адрес DNS сервера. Пример: 192.168.0.1")
                                    delay: 1000
                                }
                            }
                            Rectangle {
                                // id: modelIpError
                                anchors.fill: parent
                                color: "#00FF0055"
                                visible: true
                            }
                        }
                        RadioButton {
                            text: "Является первичным DNS сервером домена?"
                            checked: model.is_auto_resolv  
                            ButtonGroup.group: radioGroup                  
                        }
                    }
                }
            }
            Button {
                text: "Добавить DNS сервер"
                onClicked: { 
                    modelTest.append({ip: "", host: "", is_auto_resolv: true})
                    // ++dns_list.model
                    // dns_list.itemAt(0)
                    // PyConsole.log("test")
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
                Rectangle {
                    id: hostnameError
                    anchors.fill: parent
                    color: "#00FF0055"
                    visible: true
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
                Rectangle {
                    id: time_serverError
                    anchors.fill: parent
                    color: "#00FF0055"
                    visible: true
                }
            }
            Button {
                text: qsTr("Применить настройки")
                width: parent.width
                onClicked: {
                    mainView.enabled = false
                    if (validate()) {
                        // TODO: search why doen't work
                        // dns_list.model.sync()
                        // var test = MVjs.dns_listToList(dns_list.model)
                        var dns_array = []
                        for(var i = 0; i < dns_list.model.count; ++i) {
                            var host = dns_list.itemAt(i).children[0].children[1]
                            var ip = dns_list.itemAt(i).children[1].children[1]
                            var is_admin_server = dns_list.itemAt(i).children[2].children[1]
                            dns_array.push({
                                host: host.text,
                                ip: ip.text,
                                is_admin_server: is_admin_server.checked,
                            }) 
                        }
                        mainController.update_configs(is_auto_resolv.checked, is_dhcp.checked, domain.text, dns_array, hostname.text, time_server.text)
                        mainView.enabled = true
                        completeDialog.open()
                    } else {
                        mainView.enabled = true
                        failDialog.open()
                    }
                }
            }
        }
    }
    function validate() {
        var is_valid = true
        if (domain.text.length == 0) {
            domainError.color = "#55FF0055"
            is_valid = false
        } else {
            domainError.color = "#00FF0055"
        }
        if (hostname.text.length == 0) {
            hostnameError.color = "#55FF0055"
            is_valid = false
        } else {
            hostnameError.color = "#00FF0055"
        }
        if (time_server.text.length == 0) {
            time_serverError.color = "#55FF0055"
            is_valid = false
        } else {
            time_serverError.color = "#00FF0055"
        }
        
        var test = []
        var count = dns_list.model.count
        for(var i = 0; i < count; ++i) {
            var host = dns_list.itemAt(i).children[0].children[1]
            var ip = dns_list.itemAt(i).children[1].children[1]

            var hostError = dns_list.itemAt(i).children[0].children[2]
            var ipError = dns_list.itemAt(i).children[1].children[2]
            
            if (host.text.length == 0) {
                hostError.color = "#55FF0055"
                is_valid = false
            } else {
                hostError.color = "#00FF0055"
            }
            if (ip.text.length == 0) {
                ipError.color = "#55FF0055"
                is_valid = false
            } else {
                ipError.color = "#00FF0055"
            }
            var ip_list = ip.text.split(".")
            if (ip_list.length < 4 ) {
                ipError.color = "#55FF0055"
                is_valid = false
            } else {
                var valid_ip = ""
                for(var i = 0; i < 4; ++i) {
                    valid_ip += parseInt(ip_list[i], 10).toString()
                    if (i < 3) {
                        valid_ip += "."
                    }
                }
                if (ip.text != valid_ip) {
                    ipError.color = "#55FF0055"
                    is_valid = false
                } else {
                    ipError.color = "#00FF0055"
                }
            }
        }
        return is_valid
    }
    MessageDialog {
        id: completeDialog
        title: "Готово"
        text: "Настройки обновлены"
    }
    MessageDialog {
        id: failDialog
        title: "Ошибка"
        text: "Некоторые поля заполнены неправильно"
    }
}