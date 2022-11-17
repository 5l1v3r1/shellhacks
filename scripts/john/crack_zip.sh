#SHTRUST
#DESC:Get hash of ZIP password with zip2john
#USAGE:crack_zip [file]
#CMD:zip2john file

RED="\033[0;31m"
BLUE="\034[0;31m"
GREEN="\032[0;31m"
RESET="\e[0m"

if ! which zip2john > /dev/null
then
    echo "$RED[-]$RESET 'zip2john' is not installed!"
    exit
fi

zip2john $1