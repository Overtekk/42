# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    Makefile                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: roandrie <roandrie@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/02/05 16:58:06 by roandrie          #+#    #+#              #
#    Updated: 2026/02/23 15:21:06 by roandrie         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

# --------------#
#	Variables	#
# --------------#

NAME 		=		codexion

CC	 		=		cc
CFLAGS 		=		-g -Wall -Werror -Wextra -pthread #-fsanitize=thread
INCLUDE		=		-I coders

SRCS_DIR	=		coders
OBJ_DIR		=		obj

CFILES		=		main.c									\
					utils/check_arguments.c					\
					utils/check_scheduler.c					\
					utils/init_struct.c						\
					utils/exit.c							\
					utils/check_time.c						\
					utils/getter.c							\
					utils/setter.c							\
					thread_managements/create_thread.c		\
					thread_managements/create_mutex.c		\
					thread_managements/destroy.c			\
					thread_managements/chained_queue.c		\
					thread_managements/heap_queue.c			\
					simulation/monitoring.c					\
					simulation/coder.c						\
					simulation/logs.c						\
					simulation/scheduler_fifo.c				\
					simulation/scheduler_edf.c				\
					simulation/dongles_management.c			\
					debug/print_struct.c					\
					debug/print_queue.c

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
#	  TEXT		#
# --------------#

BOX_LINE		=	$(MAGENTA)━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━$(RESET)
BOX_ROD_TOP_L	=	$(MAGENTA)┏$(RESET)
BOX_ROD_BOTT_L	=	$(MAGENTA)┗$(RESET)
BOX_ROD_TOP_R	=	$(MAGENTA)┓$(RESET)
BOX_ROD_BOTT_R	=	$(MAGENTA)┛$(RESET)
BOX_ROD_MIDDLE	=	$(MAGENTA)┃$(RESET)

LINE			=	⮑

USAGE			=	$(BMAGENTA)$(BOLD) Usage:\t\t\t\t\t\t\t\t\t\t   $(RESET)
ARGUMENTS_LINE1	=	$(CYAN)$(BOLD) ./$(NAME)$(ITALIC) <number_of_coders> <time_to_burnout> <time_to_compile> <time_to_debug>$(RESET)
ARGUMENTS_LINE2	=	$(CYAN)$(BOLD)$(ITALIC)     <time_to_refactor> <number_of_compiles_required> <dongle_cooldown> <scheduler>$(RESET)

SUCCESS_COMPIL	=	$(BGREEN)Success! $(RESET)$(BGREEN)Compiling $(NAME)...
COMPILED		=	$(GREEN)$(BOLD)[Compiled] ✅ $(RESET)

CLEAN_OBJ		=	$(YELLOW)$(BOLD)$(OBJ_DIR)$(RESET)$(YELLOW) folder have been deleted 🗑️$(RESET)
CLEAN_EXEC		=	$(YELLOW)$(BOLD)$(NAME)$(RESET)$(YELLOW) executable have been cleaned 🗑️$(RESET)

# --------------#
#	  RULES		#
# --------------#

.PHONY:				all clean fclean re
.SILENT:

all:			$(NAME)

$(NAME):		$(OBJS)
					@echo "\n$(LINE) $(SUCCESS_COMPIL)$(RESET)"
					$(CC) $(CFLAGS) $(OBJS) -o $(NAME)
					@echo "$(BOX_ROD_TOP_L)$(BOX_LINE)$(BOX_ROD_TOP_R)"
					@echo "$(BOX_ROD_MIDDLE)\t\t\t\t\t\t\t\t\t\t\t   $(BOX_ROD_MIDDLE)\n$(BOX_ROD_MIDDLE)$(USAGE)$(BOX_ROD_MIDDLE)\n$(BOX_ROD_MIDDLE)$(ARGUMENTS_LINE1)\t   $(BOX_ROD_MIDDLE)\n$(BOX_ROD_MIDDLE)\t$(ARGUMENTS_LINE2)$(BOX_ROD_MIDDLE)"
					@echo "$(BOX_ROD_BOTT_L)$(BOX_LINE)$(BOX_ROD_BOTT_R)"

$(OBJ_DIR)/%.o:	$(SRCS_DIR)/%.c
					mkdir -p $(dir $@)
					@if [ ! -f $(OBJ_DIR)/.header_shown ]; then \
					touch $(OBJ_DIR)/.header_shown; \
					fi
					@echo "$(LINE) $(COMPILED)$(BLUE)\"$^\"$(RESET)"
					$(CC) $(CFLAGS) $(INCLUDE) -c $< -o $@

clean:
					rm -rf $(OBJ_DIR)
					@echo "$(LINE) $(CLEAN_OBJ)"

fclean:			clean
					rm -f $(NAME)
					@echo "$(LINE) $(CLEAN_EXEC)"

re:				fclean all
