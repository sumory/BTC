#!/bin/sh


current_share_file=$1
check_share_result="check_result"

echo "`date +%F\ %T` check "$current_share_file"..."

awk 'BEGIN{
    SUBSEP=":";
}
{  
    difficulty=$9;
    count[$3 SUBSEP $9]+=1;
}
END{
    printf "%-20s\t%8s\t%20s\t%20s\n","Name","Difficulty","Count","Shares"
    for(key in count){
        split(key,subkey,SUBSEP)
        number=count[subkey[1],subkey[2]]
        printf "%-20s\t%8s\t%20s\t%20s\n", subkey[1],subkey[2],number,(subkey[2]*number)
    }
}' $current_share_file > $check_share_result

echo "`date +%F\ %T` check finished...\n"

cat $check_share_result

echo ""
