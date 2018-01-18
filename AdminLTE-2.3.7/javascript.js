/*Aqui lo que se hace es crear las funciones para los botones del formulario*/       
        var sock = null;
        var ellog = null;
        window.onload = function() {
            var wsuri;
            ellog = document.getElementById('log');
            if (window.location.protocol === "file:") {
                wsuri = "wss://localhost:9000";
            } else {
                wsuri = "wss://192.168.1.146:9000";
            }
            if ("WebSocket" in window) {
                sock = new WebSocket(wsuri);
            } else if ("MozWebSocket" in window) {
                sock = new MozWebSocket(wsuri);
            } else {
                log("Browser does not support WebSocket!");
            }
            if (sock) {
                sock.onopen = function() {
                    log("Connected to " + wsuri);
                }
                sock.onclose = function(e) {
                    log("Connection closed (wasClean = " + e.wasClean + ", code = " + e.code + ", reason = '" + e.reason + "')");
                }
                sock.onmessage = function(e) {
                    log("Respuesta del servidor: " + e.data);
                }
            }
        };
        function user() {
            var usuario = document.getElementById('usuario').value;
            var pass = document.getElementById('pass').value;


            if (sock) {

                sock.send(JSON.stringify({action: "createUser", usuario: usuario, password: pass}));

                log("Se envio la peticion de crear usuario");
            } else {
                log("Not connected.");
            }
        };
        function folder() {
            var NombreCarpeta = document.getElementById('nombre').value;
            var ubicacion = document.getElementById('ubicacion').value;


            if (sock) {

                sock.send(JSON.stringify({action: "createFolder", name: NombreCarpeta, location: ubicacion}));

                log("Se envio la peticion de crear carpeta");
            } else {
                log("Not connected.");
            }
        };
        function restart() {
            if (sock) {

                sock.send(JSON.stringify({action: "restartSamba"}));

                log("Se envio la peticion de reinicio de samba");
            } else {
                log("Not connected.");
            }
        };
        function stop() {
            if (sock) {

                sock.send(JSON.stringify({action: "stopSamba"}));

                log("Se envio la peticion de reinicio de samba");
            } else {
                log("Not connected.");
            }
        };
        function start() {
            if (sock) {

                sock.send(JSON.stringify({action: "startSamba"}));

                log("Se envio la peticion de reinicio de samba");
            } else {
                log("Not connected.");
            }
        };
        function log(m) {
            document.getElementById('log').innerHTML += m + '\n';
        };
