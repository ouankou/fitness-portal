function prepareDataTableColumnsFromDataInstance(dataInstance) {
    let keys = Object.keys(dataInstance);
    let columns = [];
    _.forEach(keys, function (col) {
        columns.push({'data': col});
        console.log(columns);
    });
    console.log(dataInstance);
    console.log(columns);
    return columns;
}
