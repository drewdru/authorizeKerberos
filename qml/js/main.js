/**
 * Replace qml file url to path or another url
 * 
 * @param url: The file url
 * @param p1: The old prefix
 * @param p2: The new prefix
 */
function replaceUrlToPath(url, p1, p2) {
    var res = encodeURI(url);
    res = res.replace(p1,p2);
    res = decodeURI(res);
    return res;
}

/**
 * Copy image to inImage.png
 * 
 * @param fileUrl: The qml file url
 */
function openFile(fileUrl) {
    var filePrefix = ''
    if (Qt.platform.os === "windows") {
        filePrefix = "file:///"
    } else {
        filePrefix = "file://"
    }
    var filePath = replaceUrlToPath(fileUrl, filePrefix, "");
    console.log(filePath)
    mainController.openFile(filePath);
}

/**
 * Copy processingImage.png to file
 * 
 * @param fileUrl: The qml file url
 */
function saveFile(fileUrl) {
    var filePrefix = ''
    if (Qt.platform.os === "windows") {
        filePrefix = "file:///"
    } else {
        filePrefix = "file://"
    }
    var filePath = replaceUrlToPath(fileUrl, filePrefix, "");
    mainController.saveFile(filePath);
}