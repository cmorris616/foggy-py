var app = function() {

    function getServiceStatuses(callback) {
        var request = new XMLHttpRequest();

        request.onreadystatechange = function() {
            if(this.readyState != 4) {
                return;
            }

            if(this.status != 200) {
                console.error(this.status + " - " + this.statusText);
                callback({});
                return;
            }

            callback(JSON.parse(this.responseText));
        }

        request.open("GET", "/service/statuses");
        request.send();
    }

    return {
        getServiceStatuses: getServiceStatuses
    }

}