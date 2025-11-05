NAME 		=	libftprintf.a
CC 			=	cc
CFLAGS 		=	-g -Wall -Werror -Wextra

SRCS 		=	ft_printf.c				\
				ft_printchar.c			\
				ft_printstr.c			\
				ft_printnumber.c		\
				ft_print_unsi_number.c	\
				ft_print_hexa.c	\
				ft_print_ptr.c

OBJS 		=	$(SRCS:.c=.o)

LIBFT_PATH 	=	./libft
LIBFT 		=	$(LIBFT_PATH)/libft.a

.PHONY 		=	all clean fclean re libft

## RULES ##

all:			$(NAME)

%.o:			%.c
				$(CC) $(CFLAGS) -c $< -o $@

$(NAME):		$(LIBFT) $(OBJS)
				cp $(LIBFT) $(NAME)
				ar rcs $(NAME) $(OBJS)

$(LIBFT):
				make -C $(LIBFT_PATH) all
				make -C $(LIBFT_PATH) bonus

clean:
				make -C $(LIBFT_PATH) clean
				rm -f $(OBJS)

fclean:			clean
				make -C $(LIBFT_PATH) fclean
				rm -f $(NAME)

re: 			fclean all
