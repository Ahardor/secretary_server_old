const express = require('express')
const app = express()
const http = require('http')
const server = http.createServer(app)
const mysql = require('mysql')
const { Server } = require("socket.io");
const io = new Server(server);

app.get('/', (req, res) => {
    res.send('Hello');
});

io.on('connection', socket => {
    console.log('New connection')
    socket.on('disconnect', () => {
        console.log('user disconnected');
    });

    socket.on('signin', data => {
        var query = `SELECT * FROM secretary.users WHERE users.email = "${data['email']}"`

        con.query(query, (err, result, field) => {
            if(result.length > 0){
                socket.emit('signinres', result[0]['password'] == data['password'])
            }
            else socket.emit('signinres', false)
        })
    })
})

server.listen(3000, () => {
    console.log('listening on *:3000');
});

var con = mysql.createConnection( {
    host: 'localhost',
    user: 'rockus',
    password: 'markus152'
})

con.connect(function(err) {
    if(err) throw err
    console.log('Connected')
})

