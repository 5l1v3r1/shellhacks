#SHTRUST
#DESC:Quick verbose UDP version scan
#USAGE:nmap_udp [target]
#CMD:nmap -sU -sV -vv [target]

RED="\033[0;31m"
BLUE="\034[0;31m"
GREEN="\032[0;31m"
RESET="\e[0m"

if ! which nmap > /dev/null
then
    echo "$RED[-]$RESET 'nmap' is not installed!"
    exit
fi

nmap -sU -sV -vv $1