var nodemailer = require("nodemailer");
var config = require("../config.js");
var helper = require('./helper.js');
var qq_mail = config.qq_mail;

var transport = nodemailer.createTransport("SMTP", {
    service : "QQ",
    name : "asicme mail robot",
    auth : {
        user : qq_mail.user,
        pass : qq_mail.password
    }
});

exports.batchSendMail = function(sendTo, subject, content) {
    if (typeof (sendTo) === 'string') {
        sendTo = [ sendTo ];
    }

    for ( var i in sendTo) {
        var to = sendTo[i];
        sendMail(to, subject, content, null);
    }

};

exports.sendMail = function(sendTo, subject, content, callback) {
    var mainOptions = {
        from : "ASICME Mining Pool <" + qq_mail.user + ">",
        to : sendTo,
        subject : subject || '',
        html : content || ''
    };

    transport.sendMail(mainOptions, function(error, responseStatus) {
        var now = helper.now();
        if (error) {
            console.error(now + ' 邮件发送失败: ' + sendTo + ' '+content);
            console.error(now + ' 邮件发送失败Error: ', error);
            callback && callback(e);
        }
        else {
            console.log(now + ' 邮件发送成功: ' + sendTo + ' '+content+" "+ responseStatus.message);
            callback && callback(null);
        }
    });
   
};

exports.closeTransport = function() {
    transport.close();
};

function test() {
    exports.sendMail(["290118608@qq.com"], "矿池测试邮件", "<h1>你的矿工已长时间未连接矿池</h1><p><b>How</b> are you?");
    //exports.closeTransport();
}

//test();
