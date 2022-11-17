#SHTRUST
#DESC:Get hash of SSH private key with ssh2john
#USAGE:crack_ssh [file]
#CMD:/usr/share/john/ssh2john.py file

RED="\033[0;31m"
BLUE="\034[0;31m"
GREEN="\032[0;31m"
RESET="\e[0m"

if ! locate ssh2john.py > /dev/null
then
    echo "$RED[-]$RESET 'ssh2john' is not installed!"
    exit
fi

/usr/share/john/ssh2john.py $1