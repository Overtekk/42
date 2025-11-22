NAME		=		libft.a
CC			=		cc
CFLAGS		=		-g -Wall -Werror -Wextra

INC_DIR		=		include

SRC_DIR 	=		src
SRCS 		=		$(wildcard $(SRC_DIR)/*.c)

OBJ_DIR		=		obj
OBJS 		=		$(patsubst $(SRC_DIR)/%.c, $(OBJ_DIR)/%.o, $(SRCS))

BLUE			:=	\033[96m
GREEN			:=	\033[32m
MAGENTA			:=	\033[38;5;206m
BOLD			:=	\033[1m
RESET			:=	\033[0m

## RULES ##

.PHONY:				all clean fclean re
.SILENT:

all:				$(NAME)

$(NAME):			$(OBJS)
					@echo "$(BLUE)Compiled with $(GREEN)$(BOLD)$(CC) $(CFLAGS)$(RESET)"
					@echo "$(MAGENTA)-----------------------------------------------$(RESET)"
					@echo "	$(BLUE)$(BOLD)$(NAME)$(RESET)$(BLUE) NOW READY FOR USE!"
					@echo "$(MAGENTA)-----------------------------------------------$(RESET)"
					ar rcs $(NAME) $(OBJS)

$(OBJ_DIR)/%.o:		$(SRC_DIR)/%.c
					@mkdir -p $(OBJ_DIR)
					@echo "$(BLUE)$(BOLD)[Compiled] ✅ $(GREEN)\"$^\"$(RESET)"
					$(CC) $(CFLAGS) -I$(INC_DIR) -c $< -o $@

clean:
					rm -rf $(OBJ_DIR)

fclean:				clean
					rm -f $(NAME)
					@echo "$(BLUE) $(BOLD)$(NAME) $(RESET)$(BLUE)have been cleaned 🗑️$(RESET)"

re:					fclean $(NAME)
