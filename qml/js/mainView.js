
/**
 * List model to list
 * 
 * @param listModel: QQmlListModel
 */
function dns_listToList(listModel) {
    var objects_list = []
    console.log(listModel)
    for(var i = 0; i < listModel.count; ++i) {
        console.log(listModel.get(i))
        console.log(listModel.get(i).host)
        console.log(listModel.get(i).ip)
        objects_list.push({
            host: listModel.get(i).host,
            ip: listModel.get(i).ip,
        })
    }
    console.log(objects_list)
    return objects_list
}