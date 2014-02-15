var schedule = require('node-schedule');
var async = require('async');
var _ = require('underscore');

var helper = require('./lib/helper.js');
var mysql = require('./lib/mysql.js');
var sms = require('./lib/sms.js');
var mail = require('./lib/mail.js');

var main_db = mysql.main;
var pool_db = mysql.pool;

var timeout = 30 * 60 * 1000;// 30分钟，毫秒数

// 每1分钟执行一次
var j = schedule.scheduleJob('*/1 * * * *', function() {
    console.log(helper.now(), '\n执行一分钟任务');
    //check();
});

setInterval(function(){
    check();
}, 3000);

function check() {
    async.parallel({
        workers : function(callback) {// 按worker_name获取每个worker的最后活跃时间
            pool_db.query('select worker_name, max(logTime) as last_share_time from pool_hashrate group by worker_name', [], function(err, workers) {
                if (err) {
                    console.log(err);
                    callback(null, []);
                }
                else {
                    callback(null, workers);
                }
            });
        },
        users : function(callback) {// 开放了通知功能的矿池用户
            pool_db.query('select id, user_id,username,notify_type,notify_last_time from pool_account where is_notify_open = ?', [ 1 ], function(err, poolAccounts) {
                if (err) {
                    console.log(err);
                    callback(null, []);
                }
                else {
                    callback(null, poolAccounts);
                }
            });
        }
    }, function(err, results) {
        var users = results.users;
        var workers = results.workers;
        if (users.length !== 0 && workers.length !== 0) {
            async.waterfall([ function(callback) {

                // 获取用户，以及它的最后一个share的提交时间
                var userLastShareTimeMap = {};// key: 用户, value: 他最后一个share的提交时间
                for ( var w in workers) {
                    var worker = workers[w];
                    var username = worker['worker_name'].split('.')[0];// 取得username
                    var lastShareTime = worker['last_share_time'];
                    if (userLastShareTimeMap[username]) {
                        if (lastShareTime > userLastShareTimeMap[username]) {
                            userLastShareTimeMap[username] = lastShareTime;
                        }
                    }
                    else {
                        userLastShareTimeMap[username] = lastShareTime;
                    }
                }

                var now = new Date();

                // 计算开放了通知功能并满足发送通知要求的用户
                var toNotifyUsers = _.filter(users, function(u) {
                    var lastShareTime = userLastShareTimeMap[u['username']];
                    var notifyLastTime = u['notify_last_time'];
                    console.log('比较', u['username'], helper.date(notifyLastTime), helper.date(lastShareTime));

                    if (!notifyLastTime) {
                        if (lastShareTime && now - lastShareTime > timeout)
                            return true;
                        else
                            return false;
                    }
                    else {
                        if (lastShareTime && now - lastShareTime > timeout && lastShareTime > notifyLastTime)
                            return true;
                        else
                            return false;
                    }

                    return false;
                });

                callback(null, toNotifyUsers);

            } ], function(err, toNotifyUsers) {

                if (!err) {
                    var toNotifyUsernames = _.map(_.pluck(toNotifyUsers, 'username'), function(item) {
                        return '"' + item + '"';
                    });
                    
                    if(!toNotifyUsernames || toNotifyUsernames.length==0){
                        console.log('没有需要通知的用户');
                        return;
                    }
                    
                    main_db.query('select id, username, tel, email, tel_active, email_active from user where username in (' + toNotifyUsernames.join(',') + ')', [], function(err, userList) {
                        //console.log('最终要发通知的用户：');
                        if (err) {
                            console.log(err);
                        }
                        else {
                            var poolAccountsByUsername = _.indexBy(toNotifyUsers, 'username');
                            //console.dir(poolAccountsByUsername);// 要通知的具体账户
                            _.each(userList, function(u) {
                                var username = u['username'];
                                var poolAccount = poolAccountsByUsername[u['username']];// 该用户的矿池账户
                                var id = poolAccount.id;
                                var now = new Date();
                                var notify_type = poolAccount['notify_type'];// 矿池提醒的方式,用|连接 0为短信 1为邮件'
                                console.log('发给用户',username,u['tel_active'] ,u['email_active'], notify_type);
                                if (notify_type) {
                                    if (notify_type.indexOf('0') !== -1 && u['tel_active'] == 1 && u['tel']) {
                                        var tel = u['tel'];//'13693320901';// u['tel'];
                                        if(username.length>12){
                                            username = username.substring(0,12)+'..';
                                        }
                                        sms.sendSMS(tel, '尊敬的ASICME矿池用户'+username+'，您的矿机已离线超过30分钟，按照您的设置特此提醒【asicme.com】', function(e){
                                            if(!e){
                                                pool_db.query('update pool_account set notify_last_time=? where id= ?',[now, id],function(err,data){});
                                            }
                                        });//52个字符加用户名
                                    }
                                    if (notify_type.indexOf('1') !== -1 && u['email_active'] == 1 && u['email']) {
                                        var email = u['email'];//'echover@qq.com';// u['email'];
                                        mail.sendMail(email, '来自ASICME矿池的提醒', '尊敬的ASICME矿池用户【' + username + '】您好，您的矿机已经超过30分钟未连接到矿池，按照您的通知设置，特此邮件提醒!【asicme.com】', function(e){
                                            if(!e){
                                                pool_db.query('update pool_account set notify_last_time=? where id= ?',[now, id],function(err,data){});
                                            }
                                        });
                                    }
                                }
                            });
                        }
                    });
                }
            });
        }
    });

}


