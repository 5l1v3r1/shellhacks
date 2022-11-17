#SHTRUST
#DESC:Directory brute force with common.txt
#USAGE:dir_common [url]
#CMD:gobuster dir -w /usr/share/wordlists/dirb/common.txt -u url

RED="\033[0;31m"
BLUE="\034[0;31m"
GREEN="\032[0;31m"
RESET="\e[0m"

if ! which gobuster > /dev/null
then
    echo "$RED[-]$RESET 'gobuster' is not installed!"
    exit
fi

gobuster dir -w /usr/share/wordlists/dirb/common.txt -u $1