var app = function() {

    function getServiceStatuses(callback) {
        var request = new XMLHttpRequest();

        request.onreadystatechange = function() {
            if(this.readyState != 4) {
                return;
            }

            if(this.status != 200) {
                callback({});
                return;
            }

            callback(JSON.parse(this.responseText));
        }

        request.open("GET", "/service/statuses");
        request.send();
    }
	
    function loadHeader() {
        var request = new XMLHttpRequest();

        request.onreadystatechange = function() {
            if(this.readyState != 4) {
                return;
            }

            if(this.status != 200) {
                console.error(this.status + " - " + this.statusText);
                return;
            }

            document.body.innerHTML = this.responseText + document.body.innerHTML;
        }

        request.open("GET", "/static/header.html");
        request.send();
    }
    
    loadHeader();

    return {
        getServiceStatuses: getServiceStatuses
    }

}