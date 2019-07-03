#!/bin/bash
for i in {00..99};do
    echo -ne "id: ${i}\r"
    sleep 1
done
