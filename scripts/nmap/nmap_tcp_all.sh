#SHTRUST
#DESC:All ports verbose TCP version scan
#USAGE:nmap_tcp_all [target]
#CMD:nmap -sT -sV -p- -vv [target]

RED="\033[0;31m"
BLUE="\034[0;31m"
GREEN="\032[0;31m"
RESET="\e[0m"

if ! which nmap > /dev/null
then
    echo "$RED[-]$RESET 'nmap' is not installed!"
    exit
fi

nmap -sT -p- -vv $1