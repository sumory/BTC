var helper = require('./lib/helper.js');
var sms = require('./lib/sms.js');
var exec = require('child_process').exec;


setInterval(function() {
    monitor();
}, 50000);


var port = 8888;

function monitor() {
var now = helper.now();
//console.log(now);
exec("netstat -anp | grep " + port + " | wc -l", function(err, all_count) {
    exec("netstat -anp | grep " + port + " | grep CLOSE_WAIT | wc -l", function(err, close_wait_count) {
        if (!err) {
            //console.log('close wait count: ', close_wait_count);
            exec("netstat -anp | grep " + port + " | grep LAST_ACK | wc -l", function(err, last_ack_count) {
                if (!err) {
                    //console.log('last ack count: ', last_ack_count);
                    var total_danger = parseInt(close_wait_count) + parseInt(last_ack_count);
                    if(total_danger>=150){
                        var msg = now + ' 矿池故障,tcp连接: ALL:' + all_count + ' WAIT:'+close_wait_count+' ACK:'+last_ack_count;
                        //遇到不可预知错误导致服务故障时短信通知
                        send(msg);

                        if(total_danger>=250){
                            exec("kill -9 `ps aux | grep 'python server.py' | grep -v grep | awk '{print $2}'`", function(err, result){
                                send(now + ' 杀掉了server.py, total_danger:'+total_danger);
                            });

                        
                        }
                    }
                }
            });
        }
    });
});


}


function send(msg) {
    sms.sendSMS('*****', msg, function(e) {});//往我的手机发送提示信息
}
