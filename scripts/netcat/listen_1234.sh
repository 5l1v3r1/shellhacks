#SHTRUST
#DESC:Listen port 1234
#USAGE:listen_1234
#CMD:nc -lnvp 1234

RED="\033[0;31m"
BLUE="\034[0;31m"
GREEN="\032[0;31m"
RESET="\e[0m"

if ! which nc > /dev/null
then
    echo "$RED[-]$RESET 'nc' is not installed!"
    exit
fi

nc -lnvp 1234