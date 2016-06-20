#!/bin/bash

MSG_KEY=93714013
ALIAS_KEY=qwerty
ALIAS_VALUE=127.0.0.1
TEST_OUT=simplemail_test.out

echo "TEST RESULTS" > ${TEST_OUT}

check()
{
if [ $? -eq 0 ];
    then echo 'PASS', $1;
    else echo 'FAIL', $1;
fi
}

simplemail all ${MSG_KEY} >> ${TEST_OUT}
check 1
simplemail inbox >> ${TEST_OUT}
check 2
simplemail inbox | grep ${MSG_KEY} >> ${TEST_OUT}
check 3
simplemail delete 0 | grep -v ${MSG_KEY} >> ${TEST_OUT}
check 4
simplemail alias ${ALIAS_KEY} ${ALIAS_VALUE} >> ${TEST_OUT}
check 5
simplemail alias >> ${TEST_OUT}
check 6
simplemail alias | grep "${ALIAS_KEY} ${ALIAS_VALUE}" >> ${TEST_OUT}
check 7