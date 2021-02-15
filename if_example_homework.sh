#! /bin/bash

# Link for checking the number of arguments!
# https://stackoverflow.com/questions/18568706/check-number-of-arguments-passed-to-a-bash-script

# Stores the input of the user into two variables.
input1=$1
input2=$2


# An if statment where if number of args is more or less than 2. Send an error messgage. 
# If not, get the sum of those numbers
if [ "$#" -ne 2 ]; then
    echo "Error! $# argument(s), need exactly two args "

else
    sum=$(( $input1 + $input2))
    echo "Output: Sum is = $sum"
fi
