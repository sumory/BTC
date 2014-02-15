awk '{count++;print count" "$1;cmd="bitcoind addnode "$1" onetry";cmd|getline;}' $1
