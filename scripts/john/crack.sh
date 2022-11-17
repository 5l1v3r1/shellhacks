#SHTRUST
#DESC:Crack hash with rockyou.txt
#USAGE:crack [hash]
#CMD:john --wordlist=/usr/share/wordlists/rockyou.txt .temp_hash

RED="\033[0;31m"
BLUE="\034[0;31m"
GREEN="\032[0;31m"
RESET="\e[0m"

if ! which john > /dev/null
then
    echo "$RED[-]$RESET 'john' is not installed!"
    exit
fi

echo "$1" > .temp_hash
john --wordlist=/usr/share/wordlists/rockyou.txt .temp_hash
rm .temp_hash