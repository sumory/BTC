var util = require('util');
var mysql = require('mysql');
var config = require('../config.js');

var mysqls = {};
var dbs = config.dbs || {};
for(var i in dbs){
    console.log('init pool with config: ', i);
    mysqls[i] = new Mysql(dbs[i]);
}

module.exports = exports = mysqls;

// Mysql 
function Mysql(db_config){
    this.pool = undefined;
    var config = db_config || null;
    if(!config){
        console.error('init mysql pool error: no configuration given.');
        process.exit(1);
    }
    else{
        console.log("init mysql pool start..");
        this.pool  = mysql.createPool({
            host: config.server,
            port: config.port,
            user: config.user,
            password: config.password,
            database: config.database,
            supportBigNumbers: config.supportBigNumbers || true,// 是否支持处理大数 (BIGINT 和 DECIMAL)
            bigNumberStrings: config.bigNumberStrings || true,// 与supportBigNumbers配合，BIGINT和DECIMAL都以string形式返回
            debug: config.debug || false
        });
        console.log("init mysql pool end....");
    }
}

Mysql.prototype.query = function (sql, params, callback) {
    var pool = this.pool;
    if (util.isArray(params)) {
        pool.getConnection(function (err, connection) {// query有三个参数，分别是sql(prepared),params,callback
            if (err) {
                callback(err);
                return;
            }
            else{
                connection.query(sql, params, function (err, result) {
                    connection.release();
                    callback(err, result);
                });
            }
        });
    }
    else {
        callback = params;
        pool.getConnection(function (err, connection) {// query有2个参数，分别是sql,callback
            if (err) {
                callback(err);
                return;
            }
            else{
                connection.query(sql, function (err, result) {
                    connection.release();
                    callback(err, result);
                });
            }

        });
    }
};

