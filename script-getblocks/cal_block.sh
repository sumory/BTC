#!/bin/sh

rm -rf date_block.result
rm -rf blocks.result
rm -rf sort_date_block.result

awk -F '\t' '{
    split($1, array, " ");
    height = array[3];

    print height"\t"$2"\t"$3;
}' logs/block.log > blocks.result 

awk -F '\t' '{
    height = $1;
    
    split($2, datetime, " ");
    date = datetime[1]

    if(date=="2013-10-04"){
        #print height"\t"date"\t"$2"\t"$3;
    }


    count[date]++;
}
END{
    for(c in count){
        print c"\t"count[c]
    }

}' blocks.result > date_block.result

sort -k 1 -r date_block.result > sort_date_block.result
rm -rf date_block.result
