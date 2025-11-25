NAME			=	so_long
CC				=	cc
CFLAGS			=	-g -Wall -Werror -Wextra
MLXFLAGS		=	-L $(MINILIBX_PATH) -lmlx -lXext -lX11

LIBFT_PATH		=	./libft
MINILIBX_PATH	=	./minilibx-linux

LIBFT			=	$(LIBFT_PATH)/libft.a
MINILIBX		=	$(MINILIBX_PATH)/libmlx.a

INCLUDE			=	-I${LIBFT_PATH}/include -I$(MINILIBX_PATH) -I./include

SRCS_DIR		=	sources
C_FILE			=	main.c					\
					init_map.c				\
					check_map.c				\
					check_invalid_path.c	\
					init_game.c				\
					stop_game.c				\
					free_memory.c			\
					print_errors.c			\
					debug.c
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

$(MINILIBX):
				@echo "$(MAGENTA)>>>"
				@echo "	$(BRED)STARTING CREATING $(BOLD)minilibx.a$(RESET)"
				@echo "$(MAGENTA)>>>$(RESET)"
				@make -C $(MINILIBX_PATH) --no-print-directory

$(OBJ_DIR):
				mkdir -p $(OBJ_DIR)

$(NAME):		$(LIBFT) $(MINILIBX) $(OBJ_DIR) $(OBJS)
				@echo "$(BLUE)Compiled with $(GREEN)$(BOLD)$(CC) $(CFLAGS)$(MLXFLAGS)$(RESET)"
				$(CC) $(CFLAGS) $(OBJS) $(LIBFT) $(MLXFLAGS) -o $(NAME)
				@echo "$(MAGENTA)-----------------------------------------------$(RESET)"
				@echo "    $(BLUE)YOU CAN NOW USE $(BOLD)\"./$(NAME) maps/*.ber\"$(RESET)"
				@echo "$(MAGENTA)-----------------------------------------------$(RESET)"

$(OBJ_DIR)/%.o:	$(SRCS_DIR)/%.c
				mkdir -p $(OBJ_DIR)
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
				@make -C ${MINILIBX_PATH} clean --no-print-directory > /dev/null 2>&1
				@echo "$(BLUE) $(BOLD)$(OBJ_DIR) $(RESET)$(BLUE)have been deleted 🗑️$(RESET)"

fclean:			clean
				@make -C $(LIBFT_PATH) fclean --no-print-directory
				rm -f $(NAME)
				@echo "$(BLUE) $(BOLD)$(NAME) $(RESET)$(BLUE)have been cleaned 🗑️$(RESET)"

re:				fclean all

