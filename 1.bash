#!/bin/bash

if [ -e $1 ]
then
    echo "file exists"
    test -w $1 && echo "Writable" || echo "Not Writable"
    ls -l $1
else
    echo "file does not exist"
fi


