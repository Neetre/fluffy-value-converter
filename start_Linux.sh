#!/bin/bash

source ./setup/setup_Linux.shù

clear

echo "Do you want to run the program in GUI mode? (y/n):"
read UserInput

cd /bin/

if [ $UserInput = "n" ]; then
    python3 converter.py --cli
    exit
fi

python3 converter.py --gui
exit