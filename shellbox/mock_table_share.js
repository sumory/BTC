var fs = require('fs');
var path = require('path');

var log = 'share.log';

function now(){
    var date = new Date();
    var year = date.getFullYear();
    var month = date.getMonth() + 1;
    var day = date.getDate();
    var hour = date.getHours();
    var minute = date.getMinutes();
    var second = date.getSeconds();
    month = ((month < 10) ? '0' : '') + month;
    day = ((day < 10) ? '0' : '') + day;
    hour = ((hour < 10) ? '0' : '') + hour;
    minute = ((minute < 10) ? '0' : '') + minute;
    second = ((second < 10) ? '0' : '') + second;

    return year + '-' + month + '-' + day + ' ' + hour + ':' + minute + ':' + second;
}

var writer = fs.createWriteStream(log, {
    flags:'w',
    encoding:'utf8'
});


for(var count=0;count<1000;count++){//1000个用户
    for(var worker=1;worker<=5;worker++){//每个用户5个worker
        var user='vuser_'+count+'.worker_'+worker;

        for(var i=1;i<=22;i++){
            var tmp=i;
            var pps='0.00000021';
            if(i<10){
                tmp='0'+i;
                pps='0.00000027';
            }
            var date='201309'+tmp;

            var radios=[0.90,0.92,0.93];
            var updateTimes=['03:30:00','16:00:00','23:59:59'];
            for(var r=0;r<radios.length;r++){//假设一天调整了3次计算count的比率
                var real_count = Math.ceil(Math.random()*200000000);//2亿
                var updateTime = '2013-09-'+tmp+' '+updateTimes[r];
                var radio=radios[r];
                var show_count=parseInt(real_count*0.92);
                var row=user+'\t'+real_count+'\t'+show_count+'\t'+radio+'\t'+date+'\t'+updateTime+'\t'+pps;
                writer.write(row+'\n');
            }
    
         }
    }
}

writer.end('');
writer.on('finish', function() {
  console.error('all writes are now complete.');
});
