NAME			=	so_long
CC				=	cc
CFLAGS			=	-g3 -Wall -Werror -Wextra
MLXFLAGS		=	-L $(MINILIBX_PATH) -lmlx -lXext -lX11

LIBFT_PATH		=	./libft
MINILIBX_PATH	=	./minilibx-linux

LIBFT			=	$(LIBFT_PATH)/libft.a
MINILIBX		=	$(MINILIBX_PATH)/libmlx.a

INCLUDE			=	-I${LIBFT_PATH}/include -I$(MINILIBX_PATH) -I./include

SRCS_DIR		=	sources
C_FILE			=	main.c				\
					ft_print_error.c	\
SRCS			=	$(addprefix $(SRCS_DIR)/, $(C_FILE))

OBJ_DIR			=	obj
OBJS			=	$(patsubst $(SRCS_DIR)/%.c, $(OBJ_DIR)/%.o, $(SRCS))

## RULES ##

.PHONY			=	all clean fclean re

all:			$(NAME)

$(LIBFT):
				make -C $(LIBFT_PATH)

$(MINILIBX):
				make -C $(MINILIBX_PATH)

$(OBJ_DIR):
				mkdir -p $(OBJ_DIR)

$(NAME):		$(LIBFT) $(MINILIBX) $(OBJ_DIR) $(OBJS)
				$(CC) $(CFLAGS) $(OBJS) $(LIBFT) $(MLXFLAGS) -o $(NAME)

$(OBJ_DIR)/%.o:	$(SRCS_DIR)/%.c
				mkdir -p $(OBJ_DIR)
				$(CC) $(CFLAGS) $(INCLUDE) -c $< -o $@

clean:
				rm -rf $(OBJ_DIR)
				make -C $(LIBFT_PATH) clean
				make -C ${MINILIBX_PATH} clean

fclean:			clean
				make -C $(LIBFT_PATH) fclean
				rm -f $(NAME)

re:				fclean all
