var mysql = require('../lib/mysql.js');
var db_main = mysql.main;

db_main.query('select * from user limit 0,2', function(err, rows) {
    console.error(err);
    console.dir(rows);
    process.exit(1);
});

