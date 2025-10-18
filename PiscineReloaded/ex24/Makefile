NAME = libft.a
CC = gcc
CFLAGS = -Wall -Wextra -Werror
INCLUDES = includes

SRCS = srcs/ft_putchar.c srcs/ft_swap.c srcs/ft_putstr.c srcs/ft_strlen.c srcs/ft_strcmp.c
OBJS = $(SRCS:.c=.o)

# tell rules are not file
.PHONY: all clean fclean re

%.o: %.c
	${CC} ${CFLAGS} -I ${INCLUDES} -c $< -o $@
# $@ = name of the file
# $< the first dependance // $^ all dependances

$(NAME): ${OBJS}
	ar rcs ${NAME} ${OBJS}

# compile
all:
	${NAME}

# delete .o
clean:
	rm -f ${OBJS}

# delete .o and file
fclean: clean
	rm -f ${NAME}

re:	fclean all
