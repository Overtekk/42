# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    Makefile                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: roandrie <roandrie@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/02/05 16:58:06 by roandrie          #+#    #+#              #
#    Updated: 2026/02/05 17:32:30 by roandrie         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

# --------------#
#	Variables	#
# --------------#

NAME 		=		codexion

CC	 		=		cc
CFLAGS 		=		-g -Wall -Werror -Wextra
INCLUDE		=		-I coders

SRCS_DIR	=		coders
OBJ_DIR		=		obj

CFILES		=		main.c

OBJS		=		$(addprefix $(OBJ_DIR)/, $(CFILES:.c=.o))

# --------------#
#	  Colors	#
# --------------#

BLUE		:=		\033[96m
MAGENTA		:=		\033[38;5;206m
BRED		:=		\e[1;31m
BOLD		:=		\033[1m
RESET		:=		\033[0m

# --------------#
#	  RULES		#
# --------------#

.PHONY:				all clean fclean re
.SILENT:

all:			$(NAME)

$(NAME):		$(OBJS)
					@echo "$(BLUE)Starting compiling $(BOLD)$(NAME)... $(RESET)"
					$(CC) $(CFLAGS) $(OBJS) -o $(NAME)
					@echo "$(MAGENTA)-----------------------------------------------$(RESET)"
					@echo "    $(BLUE)Usage $(BOLD)\"./$(NAME) [arg]\"$(RESET)"
					@echo "$(MAGENTA)-----------------------------------------------$(RESET)"

$(OBJ_DIR)/%.o:	$(SRCS_DIR)/%.c
					mkdir -p $(dir $@)
					@if [ ! -f $(OBJ_DIR)/.header_shown ]; then \
					echo "$(MAGENTA)>>>$(RESET)"; \
					echo "  $(BRED)STARTING COMPILATION$(RESET)"; \
					echo "$(MAGENTA)<<<$(RESET)"; \
					touch $(OBJ_DIR)/.header_shown; \
					fi
					@echo "$(BLUE)$(BOLD)[Compiled] ✅ $(GREEN)\"$^\"$(RESET)"
					$(CC) $(CFLAGS) $(INCLUDE) -c $< -o $@

clean:
					rm -rf $(OBJ_DIR)
					@echo "$(BLUE) $(BOLD)$(OBJ_DIR) $(RESET)$(BLUE)have been deleted 🗑️$(RESET)"

fclean:			clean
					rm -f $(NAME)
					@echo "$(BLUE) $(BOLD)$(NAME) $(RESET)$(BLUE)have been cleaned 🗑️$(RESET)"

re:				fclean all
