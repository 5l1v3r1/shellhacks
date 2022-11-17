#SHTRUST
#DESC:Directory brute force with directory-list-2.3-medium.txt
#USAGE:dir [url]
#CMD:gobuster dir -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -u url

RED="\033[0;31m"
BLUE="\034[0;31m"
GREEN="\032[0;31m"
RESET="\e[0m"

if ! which gobuster > /dev/null
then
    echo "$RED[-]$RESET 'gobuster' is not installed!"
    exit
fi

gobuster dir -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -u $1