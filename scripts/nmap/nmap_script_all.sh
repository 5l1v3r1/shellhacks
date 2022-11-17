#SHTRUST
#DESC:All ports verbose script and version scan
#USAGE:nmap_script_all [target]
#CMD:nmap -sC -sV -p- -vv [target]

RED="\033[0;31m"
BLUE="\034[0;31m"
GREEN="\032[0;31m"
RESET="\e[0m"

if ! which nmap > /dev/null
then
    echo "$RED[-]$RESET 'nmap' is not installed!"
    exit
fi

nmap -sC -sV -p- -vv $1