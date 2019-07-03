#!/bin/bash
astr="|-->"
for i in {0..60}
do
    echo -ne "\033[65G$i%"
    echo -ne "\033[${i}G${astr}"
    sleep 0.3
done
