#!/bin/bash

RED='\033[0;31m'
NC='\033[0m'

PROG="./codexion"

if [ -z "$1" ]; then
    echo -e "${RED}Missing test number.${NC}"
    echo "Usage: ./tester.sh <1>"
    exit 1
fi

VALGRIND=""
if [ "$2" == "mem" ]; then
    VALGRIND="valgrind --leak-check=full --show-leak-kinds=all --track-origins=yes"
fi

run_test() {
	echo -e "Test $1 : $2\n"
	$VALGRIND $PROG $2
}

#  <number_of_coders> <time_to_burnout> <time_to_compile> <time_to_debug> <time_to_refactor>
#  <number_of_compiles_required> <dongle_cooldown> <scheduler>


case "$1" in
	1)
        run_test 1 "4 800 200 200 200 5 10 fifo"
        ;;
    2)
        run_test 2 "4 800 200 200 200 5 10 edf"
        ;;
    2)
        run_test 2 "10 10000 100 100 100 20 50 fifo"
        ;;
	*)
        echo -e "${RED}Unkown test.${NC}"
        ;;
esac
