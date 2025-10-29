/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   main.c                                             :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: roandrie <roandrie@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/29 09:10:35 by roandrie          #+#    #+#             */
/*   Updated: 2025/10/29 15:21:58 by roandrie         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "ft_printf.h"
#include <stdio.h>

#define	RESET		"\033[0m"
#define	UNDERLINE	"\033[4m"
#define	CYAN		"\033[36m"
#define	GREEN		"\033[32m"
#define	RED			"\033[31m"

int main()
{
	int				count = 0;
	char 			c = 'a';
	// char			*str = "Hello!";
	// int				n = 1;
	// unsigned	int	unsigned_dec = 8;
	// unsigned	int	unsigned_dec_neg = -8;
	// void	*ptr = &n;

	printf(RED"\n--- Printf vs ft_printf ---\n"RESET);
	sleep (1);

// ### TEST EMPTY PRINT ### ///
	printf(UNDERLINE"\n-Print empty-\n\n"RESET);
	count = ft_printf("");
	printf("\nCount = %d\n", count);

// ### PRINT CHARACTER ### ///
	printf(UNDERLINE"\n-Print a character-\n\n"RESET);

	while (c <= 'g')
	{
		count = 0;
		printf(CYAN"");
		printf("Printf = %c\n", c);
		count = ft_printf(GREEN "ft_printf = %c", c);
		printf(RESET"\nCount = %d\n", count);
		printf("\n");
		c++;
	}
	sleep(1);

/*
	printf("\n-Print a string-\n");
	printf("Printf = %s\n", str);
	//ft_printf(str, );
	printf("\n");
	sleep(1);

	printf("\n-Print THE VOID *-\n");
	printf("Printf = %p\n", ptr);
	//ft_printf(ptr, );
	printf("\n");
	sleep(1);

	printf("\n-Print a decimal (base 10)-\n");
	n = 0;
	while (n <= 10)
	{
		printf("Printf = %d\n", n);
		//ft_printf(n, );
		printf("\n");
		n++;
	}
	sleep(1);

	printf("\n-Print a integer (base 10)-\n");
	n = 0;
	while (n <= 10)
	{
		printf("Printf = %i\n", n);
		//ft_printf(n, );
		printf("\n");
		n++;
	}
	sleep(1);

	printf("\n-Print a unsigned decimal (base 10)-\n");
	printf("Printf (positive) = %u\n", unsigned_dec);
	//ft_printf(unsigned_dec, );
	printf("\n");
	printf("Printf (negative) = %u\n", unsigned_dec_neg);
	//ft_printf(unsigned_dec_neg, );
	printf("\n");
	sleep(1);

	printf("\n-Print a number in hexadecimal (base 16) lowercase format-\n");
	n = 0;
	while (n <= 15)
	{
		printf("Printf = %x\n", n);
		//ft_printf(n, );
		printf("\n");
		n++;
	}
	sleep(1);

	printf("\n-Print a number in hexadecimal (base 16) uppercase format-\n");
	n = 0;
	while (n <= 15)
	{
		printf("Printf = %X\n", n);
		//ft_printf(n, );
		printf("\n");
		n++;
	}
	sleep(1);

	printf("\n-Print a percent sign-\n");
	printf("Printf = %%\n");
	//ft_printf(n, );
	printf("\n");
	sleep(1);*/
}
