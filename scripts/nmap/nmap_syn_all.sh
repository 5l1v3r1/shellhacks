#SHTRUST
#DESC:All ports verbose SYN version scan
#USAGE:nmap_syn_all [target]
#CMD:nmap -sS -sV -p- -vv [target]

RED="\033[0;31m"
BLUE="\034[0;31m"
GREEN="\032[0;31m"
RESET="\e[0m"

if ! which nmap > /dev/null
then
    echo "$RED[-]$RESET 'nmap' is not installed!"
    exit
fi

nmap -sS -sV -p- -vv $1