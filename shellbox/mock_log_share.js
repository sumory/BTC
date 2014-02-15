var fs = require('fs');
var path = require('path');

//2013-09-01 11:29:45.706829 asicme.com HASH 0000000004a39a264645f90ebe7aa6f3ad92dbbaa112ce9e7446e545f4db90b1 TARGET 0000000000000041525700000000000000000000000000000000000000000000
var log = '/data/sumory/mockdata/share20130911.log';

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
var targetDate = new Date('2013-09-11 23:59:59');

var interval = setInterval(function(){
    var rightnow = new Date();
    //count++;
    var user = Math.ceil(Math.random()*1000);//1~10
    var share = now()+' asicme.machine_'+user+' HASH 0000000004a39a264645f90ebe7aa6f3ad92dbbaa112ce9e7446e545f4db90b1 TARGET 0000004152570000000000000000000000000000000000000000000000000000';
    writer.write(share + '\n');
    if(autoEnd && rightnow > targetDate){
    	console.log('-------------------');
	clearInterval(interval);
    	
	writer.end('');
    }
},1);

//writer.end('this is the end\n');
writer.on('finish', function() {
  console.error('all writes are now complete.');
});
