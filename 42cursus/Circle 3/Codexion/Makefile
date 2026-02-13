# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    Makefile                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: roandrie <roandrie@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/02/05 16:58:06 by roandrie          #+#    #+#              #
#    Updated: 2026/02/13 10:13:24 by roandrie         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

# --------------#
#	Variables	#
# --------------#

NAME 		=		codexion

CC	 		=		cc
CFLAGS 		=		-g -Wall -Werror -Wextra -pthread # -fsanitize=thread
INCLUDE		=		-I coders

SRCS_DIR	=		coders
OBJ_DIR		=		obj

CFILES		=		main.c								\
					utils/check_arguments.c				\
					utils/init_struct.c					\
					utils/exit.c						\
					utils/check_time.c					\
					utils/getter.c						\
					utils/setter.c						\
					thread_managements/create_thread.c	\
					thread_managements/create_mutex.c	\
					simulation/launch.c					\
					simulation/coder.c					\
					simulation/logs.c					\
					debug/print_struct.c

OBJS		=		$(addprefix $(OBJ_DIR)/, $(CFILES:.c=.o))

# --------------#
#	  Colors	#
# --------------#

BLUE		=		\033[96m
MAGENTA		=		\033[35m
GREEN		=		\033[32m
CYAN		=		\033[36m
YELLOW		=		\033[93m
BOLD		=		\033[1m
BGREEN		=		\033[92m
BRED		=		\033[91m
BMAGENTA	=		\033[95m
UNDERLINE	=		\033[4m
ITALIC		=		\033[3m
RESET		=		\033[0m

# --------------#
#	  RULES		#
# --------------#

.PHONY:				all clean fclean re
.SILENT:

all:			$(NAME)

$(NAME):		$(OBJS)
					@echo "\n>>> $(BGREEN)Success! $(RESET)$(BGREEN)Compiling $(NAME)... $(RESET)"
					$(CC) $(CFLAGS) $(OBJS) -o $(NAME)
					@echo "$(MAGENTA)$(UNDERLINE)__________________________________________________________________________________________$(RESET)"
					@echo "$(BMAGENTA)$(BOLD)\nUsage:\n\n$(CYAN)./$(NAME) $(ITALIC)<number_of_coders> <time_to_burnout> <time_to_compile> <time_to_debug>\n\t   <time_to_refactor> <number_of_compiles_required> <dongle_cooldown> <scheduler>\$(RESET)"
					@echo "$(MAGENTA)$(UNDERLINE)__________________________________________________________________________________________$(RESET)"

$(OBJ_DIR)/%.o:	$(SRCS_DIR)/%.c
					mkdir -p $(dir $@)
					@if [ ! -f $(OBJ_DIR)/.header_shown ]; then \
					touch $(OBJ_DIR)/.header_shown; \
					fi
					@echo ">>> $(GREEN)$(BOLD)[Compiled] ✅ $(RESET)$(BLUE)\"$^\"$(RESET)"
					$(CC) $(CFLAGS) $(INCLUDE) -c $< -o $@

clean:
					rm -rf $(OBJ_DIR)
					@echo ">>> $(YELLOW)$(BOLD)$(OBJ_DIR)$(RESET)$(YELLOW) folder have been deleted 🗑️$(RESET)"

fclean:			clean
					rm -f $(NAME)
					@echo ">>> $(YELLOW)$(BOLD)$(NAME)$(RESET)$(YELLOW) executable have been cleaned 🗑️$(RESET)"

re:				fclean all
