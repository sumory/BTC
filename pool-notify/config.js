module.exports = {
    // mail config
    qq_mail : {
        host : "smtp.exmail.qq.com",
        user : "***@asicme.com",//modify as you want
        password : "****"
    },

    // mysql config
    dbs : {
        main : {// 主数据库
            server : "192.168.0.149",
            port : 3306,
            user : "root",
            password : "123456",
            database : "asicme_com",
            maxSockets : 5
        },
        pool : {// 矿池数据库
            server : "192.168.0.149",
            port : 3306,
            user : "root",
            password : "123456",
            database : "asicme_pool",
            maxSockets : 5
        }
    }
};
