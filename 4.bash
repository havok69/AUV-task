#!/bin/bash

# Basic for loop
echo 'for loop'
numbers='1 2 3 4 5'
for number in $numbers
do
echo $number
done

# Basic while loop
echo 'while loop'
i=1
while [ $i -le 5 ]
do
echo $i
((i++))
done

# Basic until loop
echo 'until loop'
i=1
until [ $i -gt 5 ]
do
echo $i
((i++))
done
