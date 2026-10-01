#!/bin/bash

# Script to run to automatically run the moulinette for each dataset.

# - COLORS -
RESET="\e[0m"
RED="\e[0;31m"
BPURPLE="\e[1;35m"
PURPLE="\e[0;35m"

if [ -z "$1" ]; then
	printf "${RED}Usage: %s {evaluate_search|evaluate_answer}\n${RESET}" "$0"
	exit 1
fi

case "$1" in
	# evaluate_student_search_results
	evaluate_search)
		printf "${PURPLE}Running the evaluation for the student search results ...\n\n${RESET}"

		# Answered : dataset_code
		printf "🗨 Path: Answered -> dataset_code\n--------\n"
		./moulinette evaluate_student_search_results \
					 "data/output/search_results/AnsweredQuestions/dataset_code_public.json" \
					 "data/datasets/AnsweredQuestions/dataset_code_public.json" \
					 --k 10 --m 2000
		printf "\n\n"

		# Answered : dataset_code
		printf "🗨 Path: Answered -> dataset_docs\n--------\n"
		./moulinette evaluate_student_search_results \
					 "data/output/search_results/AnsweredQuestions/dataset_docs_public.json" \
					 "data/datasets/AnsweredQuestions/dataset_docs_public.json" \
					 --k 10 --m 2000
		printf "\n\n"

		# Unanswered : dataset_code
		printf "🗨 Path: Unanswered -> dataset_code\n--------\n"
		./moulinette evaluate_student_search_results \
					 "data/output/search_results/UnansweredQuestions/dataset_code_public.json" \
					 "data/datasets/AnsweredQuestions/dataset_code_public.json" \
					 --k 10 --m 2000
		printf "\n\n"

		# Unanswered : dataset_code
		printf "🗨 Path: Unanswered -> dataset_docs\n--------\n"
		./moulinette evaluate_student_search_results \
					 "data/output/search_results/UnansweredQuestions/dataset_docs_public.json" \
					 "data/datasets/AnsweredQuestions/dataset_docs_public.json" \
					 --k 10 --m 2000
		printf "\n\n"
		;;

	# evaluate_student_answers
	evaluate_answer)
		printf "${PURPLE}Running the evaluation for the student answer results ...\n\n${RESET}"

		# Answered : dataset_code
        printf "🗨 Path: Answered -> dataset_code\n--------\n"
        ./moulinette evaluate_student_answers \
                     "data/output/search_results_and_answer/AnsweredQuestions/dataset_code_public.json" \
                     "data/datasets/AnsweredQuestions/dataset_code_public.json"
        printf "\n\n"

        # Answered : dataset_docs
        printf "🗨 Path: Answered -> dataset_docs\n--------\n"
        ./moulinette evaluate_student_answers \
                     "data/output/search_results_and_answer/AnsweredQuestions/dataset_docs_public.json" \
                     "data/datasets/AnsweredQuestions/dataset_docs_public.json"
        printf "\n\n"
        ;;

	*)
		printf "${RED}Error: unkown argument '%s'.\n${RESET}" "$1"
		exit 1
		;;
esac
