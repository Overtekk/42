NAME			=	push_swap
CC				=	cc
CFLAGS			=	-g -Wall -Werror -Wextra

LIBFT_PATH		=	./libft
LIBFT			=	$(LIBFT_PATH)/libft.a

INCLUDE			=	-I${LIBFT_PATH}/include

SRCS_DIR		=	sources
C_FILE			=	main.c					\
					check_param.c			\
					sort/swap.c				\
					sort/push.c				\
					sort/rotate.c			\
					sort/reverse_rotate.c	\
					utils/list_management.c	\
					utils/ft_error.c
SRCS			=	$(addprefix $(SRCS_DIR)/, $(C_FILE))

OBJ_DIR			=	obj
OBJS			=	$(patsubst $(SRCS_DIR)/%.c, $(OBJ_DIR)/%.o, $(SRCS))

BLUE			:=	\033[96m
GREEN			:=	\033[32m
MAGENTA			:=	\033[38;5;206m
PINK			:=	\033[35m
BOLD			:=	\033[1m
RESET			:=	\033[0m
BRED			:=	\e[1;31m

## RULES ##

.PHONY:			all clean fclean re
.SILENT:

all:			$(NAME)

$(LIBFT):
				@echo "$(MAGENTA)>>>$(RESET)"
				@echo "	$(BRED)STARTING CREATING $(BOLD)libft.a$(RESET)"
				@echo "$(MAGENTA)>>>$(RESET)"
				@make -C $(LIBFT_PATH) --no-print-directory

$(NAME):		$(LIBFT) $(OBJS)
				@echo "$(BLUE)Compiled with $(GREEN)$(BOLD)$(CC) $(CFLAGS)$(RESET)"
				$(CC) $(CFLAGS) $(OBJS) $(LIBFT) -o $(NAME)
				@echo "$(MAGENTA)-----------------------------------------------$(RESET)"
				@echo "    $(BLUE)YOU CAN NOW USE $(BOLD)\"./$(NAME) int\"$(RESET)"
				@echo "$(MAGENTA)-----------------------------------------------$(RESET)"

$(OBJ_DIR)/%.o:	$(SRCS_DIR)/%.c
				mkdir -p $(dir $@)
				@if [ ! -f $(OBJ_DIR)/.header_shown ]; then \
				echo "$(MAGENTA)>>>$(RESET)"; \
				echo "	$(BRED)STARTING CREATING $(BOLD)$(NAME)$(RESET)"; \
				echo "$(MAGENTA)>>>$(RESET)"; \
				touch $(OBJ_DIR)/.header_shown; \
				fi
				@echo "$(BLUE)$(BOLD)[Compiled] ✅ $(GREEN)\"$^\"$(RESET)"
				$(CC) $(CFLAGS) $(INCLUDE) -c $< -o $@

clean:
				rm -rf $(OBJ_DIR)
				@make -C $(LIBFT_PATH) clean --no-print-directory
				@echo "$(BLUE) $(BOLD)$(OBJ_DIR) $(RESET)$(BLUE)have been deleted 🗑️$(RESET)"

fclean:			clean
				@make -C $(LIBFT_PATH) fclean --no-print-directory
				rm -f $(NAME)
				@echo "$(BLUE) $(BOLD)$(NAME) $(RESET)$(BLUE)have been cleaned 🗑️$(RESET)"

re:				fclean all
