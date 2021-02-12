#! /bin/bash

read -p "Enter Your First Number:" var1
read -p "Enter Your Second Number:" var2

sum=$(( $var1 + $var2))
product=$(( $var1 * $var2))

echo "Sum is: $sum"
echo "Product is: $product"
