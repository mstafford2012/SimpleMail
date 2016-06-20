#!/bin/bash

MSG_KEY=93714013
ALIAS_KEY=qwerty
ALIAS_VALUE=yuiop

check()
{
if [ $? -eq 0 ];
    then echo 'PASS', $1;
    else echo 'FAIL', $1;
fi
}

simplemail ${MSG_KEY}
check 1
simplemail inbox
check 2
simplemail inbox | grep ${MSG_KEY}
check 3
simplemail delete 0 | grep -v ${MSG_KEY}
check 4
simplemail alias ${ALIAS_KEY} ${ALIAS_VALUE}
check 5
simplemail alias
check 6
simplemail alias | grep ${ALIAS_KEY} ${ALIAS_VALUE}
check 7