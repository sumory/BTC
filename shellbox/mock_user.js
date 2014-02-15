var fs = require('fs');
var path = require('path');

var log = 'user.log';

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
    flags:'r+',
    encoding:'utf8'
});

var count = 0;
var autoEnd = true;

for(;count<1000;count++){
    var user='vuser_'+count;
    var row=user+'\t0b7de60cf4a0050fd5b91734a9b75deb\t0\t0\t0\t2013-09-03 23:20:18\t2013-09-03 23:20:18\t0\t0\t0\t/image/gravatar.png';
    writer.write(row+'\n');
}

writer.end('finished');
writer.on('finish', function() {
  console.error('all writes are now complete.');
});
