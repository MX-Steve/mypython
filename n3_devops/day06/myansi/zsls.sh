#!/bin/bash
id z3 &>/dev/null
if [  $? -ne 0 ] ; then
    useradd li4
    echo 321 | passwd --stdin li4
fi
