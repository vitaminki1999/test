const express = require('express');
const mysql = require('mysql');

const app = express();

const connection = mysql.createConnection({
  host: 'svc.sel5.cloudtype.app',
  port: 32712,
  user: 'root',
  password: '2024320319',
  database: 'new_schema'
});

connection.connect();

app.listen(8080, function() {
  console.log('listening on 8080');
});

app.get('/chat', function(req, res) {
  connection.query('SELECT * FROM new_table', function (error, results, fields) {
    if (error) throw error;
    res.sendFile(__dirname + '/chat.html');
  });
});

app.get('/beauty', function(req, res) {
  connection.query('SELECT * FROM new_table', function (error, results, fields) {
    if (error) throw error;
    res.send(results);
  });
});

app.get('/', function(req, res) {
  res.sendFile(__dirname + '/index.html');
});
