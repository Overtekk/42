NAME		=	push_swap
CC			=	cc

LIBFT_PATH	=	./libft
LIBFT		=	$(LIBFT_PATH)/libft.a

CFLAGS		=	-g -Wall -Werror -Wextra -I$(LIBFT_PATH)/include

SRCS		=

OBJ_DIR		=	obj
OBJS		=	$(patsubst %.c, $(OBJ_DIR)/%.o, $(SRCS))

## RULES ##

.PHONY		=	all clean fclean re libft

all:			$(NAME)

$(NAME):		$(LIBFT) $(OBJS)
				$(CC) $(CFLAGS) -o ${NAME} ${OBJS} ${LIBFT}

$(OBJ_DIR)/%.o:	%.c
				@mkdir -p $(OBJ_DIR)
				$(CC) $(CFLAGS) -c $< -o $@

$(LIBFT):
				make -C $(LIBFT_PATH) all

clean:
				rm -rf $(OBJ_DIR)
				make -C $(LIBFT_PATH) clean

fclean:			clean
				make -C $(LIBFT_PATH) fclean
				rm -f $(NAME)

re:				fclean all
