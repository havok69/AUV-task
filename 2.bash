#!/bin/bash

#the file hexa.txt is given as argument
sed -i 's/0xA0/0x50/g; s/0xFF/0x7F/g' $1
