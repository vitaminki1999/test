var mysql      = require('mysql');
var connection = mysql.createConnection({
  host     : 'svc.sel5.cloudtype.app',
  port     : 32712,
  user     : 'root',
  password : '2024320319',
  database : 'new_schema'
});
 
connection.connect();
 
connection.query('select * from new_table', function (error, results, fields) {
  if (error) throw error;
  console.log('Data from new_table', results);
});
 
connection.end();