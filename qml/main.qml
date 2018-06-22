import QtQuick 2.6
import QtQuick.Layouts 1.3
import QtQuick.Controls 2.1
import QtQuick.Controls.Material 2.1
// import QtQuick.Controls.Styles 1.4
// import QtQuick.Controls 2.1
import "js/main.js" as App
import "views"

Rectangle {

    Material.theme: Material.Dark
    Material.accent: Material.Red
    // color: Material.color(Material.BlueGrey)
    color: "white"

    id: rootWindow    
    anchors.fill: parent    
    width: 640; height: 480    
    // color: "#80000000"

    Component.onCompleted: {
    }
    
    Shortcut {
        sequence: "Ctrl+Q"
        onActivated: Qt.quit()
    }
    
    MainView {
    }

}