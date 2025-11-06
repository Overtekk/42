NAME		=		libft.a
CC			=		cc
CFLAGS		=		-g -Wall -Werror -Wextra

INC_DIR		=		include

SRC_DIR 	=		src
SRCS 		=		$(wildcard $(SRC_DIR)/*.c)

OBJ_DIR		=		obj
OBJS 		=		$(patsubst $(SRC_DIR)/%.c, $(OBJ_DIR)/%.o, $(SRCS))

## RULES ##

.PHONY:				all clean fclean re

all:				$(NAME)

$(NAME):			$(OBJS)
					ar rcs $(NAME) $(OBJS)

$(OBJ_DIR)/%.o:		$(SRC_DIR)/%.c
					@mkdir -p $(OBJ_DIR)
					$(CC) $(CFLAGS) -I$(INC_DIR) -c $< -o $@

clean:
					rm -rf $(OBJ_DIR)

fclean:				clean
					rm -f $(NAME)

re:					fclean $(NAME)
