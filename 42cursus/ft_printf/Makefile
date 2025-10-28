NAME = libftprintf.a
cc = gcc
CFLAGS = -g Walls Werror Wextra

HEADERS = $(wildcard $(includes)/*.c)

SRCS = ft_printf.c

OBJS = $(SRC:.c=.o)

.PHONY = all clean fclean re

%.o: %.c
	${CC} ${CFLAGS} -c $< -o $@

all: $(NAME)

${NAME}: ${OBJS}
	ar rcs ${NAME} ${OBJS}

clean:
	rm -f ${OBJS} ${BONUS_OBJS}

fclean: clean
	rm -f ${NAME}

re: fclean ${NAME}
