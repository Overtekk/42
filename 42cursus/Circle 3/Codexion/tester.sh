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

#  <number_of_coders>
#  <time_to_burnout> <time_to_compile> <time_to_debug> <time_to_refactor>
#  <number_of_compiles_required>
#  <dongle_cooldown> <scheduler>


case "$1" in
	1)
		run_test basic_fifo "4 800 200 200 200 5 10 fifo"
		;;
	2)
		run_test basic_edf "4 800 200 200 200 5 10 edf"
		;;
	3)
		run_test success_fifo "10 10000 100 100 100 5 50 fifo"
		;;
	4)
		run_test large_edf "20 5000 500 500 500 10 100 edf"
		;;
	5)
		run_test low_cooldown "5 2000 100 100 100 20 1 fifo"
		;;
	6)
		run_test long_actions "3 10000 2000 2000 2000 2 100 fifo"
		;;
	big)
		run_test big_test "100 10000 66 24 87 10 10 fifo"
		;;
	starvation)
		run_test starvation_case "3 1000 600 10 10 5 100 fifo"
		;;
	starvation2)
		run_test starvation_case "3 1000 600 10 10 5 100 edf"
		;;
	one_compiler_fifo)
		run_test one_compiler_fifo "1 1000 200 200 200 5 50 fifo"
		;;
	one_compiler_edf)
		run_test one_compiler_edf "1 1000 200 200 200 5 50 edf"
		;;
	zero_compile)
		run_test zero_compiles "5 1000 200 200 200 0 10 fifo"
		;;
	immediate_burnout)
		run_test immediate_burnout "2 1 200 200 200 5 10 fifo"
		;;
	cooldown_hell)
		run_test cooldown_hell "2 1000 100 100 100 5 2000 fifo"
		;;
	max_coders)
		run_test max_coders "300 10000 100 100 100 5 10 edf"
		;;
	toomany_compiler)
		run_test toomany_compiler "999 1000 200 200 200 5 50 fifo"
		;;
	error_arg1)
		run_test error_coder "banana 200 300 400 500 5 10 fifo"
		;;
	error_arg2)
		run_test error_coder "10 banana 300 400 500 5 10 fifo"
		;;
	error_arg3)
		run_test error_coder "10 200 banana 400 500 5 10 fifo"
		;;
	error_arg4)
		run_test error_coder "10 200 300 banana 500 5 10 fifo"
		;;
	error_arg5)
		run_test error_coder "10 200 300 400 banana 5 10 fifo"
		;;
	error_arg6)
		run_test error_coder "10 200 300 400 500 banana 10 fifo"
		;;
	error_arg7)
		run_test error_coder "10 200 300 400 500 5 banana fifo"
		;;
	error_arg8)
		run_test error_coder "10 200 300 400 500 5 10 banana"
		;;
	error_arg9)
		run_test error_coder "10 200 300 -400 500 5 10 edf"
		;;
	error_arg10)
		run_test error_coder "too 10 200 300 400 500 5 10 edf"
		;;
	*)
		echo -e "${RED}Unkown test.${NC}"
		;;
esac
