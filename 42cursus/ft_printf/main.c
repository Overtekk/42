/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   main.c                                             :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: roandrie <roandrie@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/29 09:10:35 by roandrie          #+#    #+#             */
/*   Updated: 2025/10/30 12:01:14 by roandrie         ###   ########.fr       */
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
	//char 			c = 'a';
	//char			*str = "Hello!";
	//char			*pstr = NULL;
	//int				n = 0;
	unsigned	int	unsigned_dec = 0;


	printf(RED"\n--- Printf vs ft_printf ---\n"RESET);
	sleep (1);
/*
// ### PRINT AN EMPTY PRINT ### ///
	printf(UNDERLINE"\n-Print empty-\n\n"RESET);
	count = ft_printf("");
	printf("\nCount = %d\n", count);

// ### PRINT CHARACTER ### ///
	printf(UNDERLINE"\n-Print a character-\n\n"RESET);

	while (c <= 'g')
	{
		count = 0;
		printf(GREEN "\nprintf =	%c\n" RESET, c);
		ft_printf(CYAN "ft_printf =	");
		count = ft_printf("%c", c);
		printf(RESET "\nChars printed > \"%d\"\n", count);
		c++;
	}
	sleep(1);
*/
/*
// ### PRINT A STRING ### ///
	printf(UNDERLINE"\n-Print a string-\n\n"RESET);

	// ## NORMAL STRING ## //
	printf(UNDERLINE"\n-Print normal string-\n\n"RESET);
	count = 0;
	printf(GREEN "\nprintf =	%s\n" RESET, str);
	ft_printf(CYAN "ft_printf =	");
	count = ft_printf("%s", str);
	printf(RESET "\nChars printed > \"%d\"\n", count);
	sleep(1);

	// ## EMPTY STRING ## //
	printf(UNDERLINE"\n-Print empty string-\n\n"RESET);
	count = 0;
	printf(GREEN "\nprintf =	%s\n" RESET, "");
	ft_printf(CYAN "ft_printf =	");
	count = ft_printf("%s", "");
	printf(RESET "\nChars printed > \"%d\"\n", count);
	sleep(1);

	// ## EMPTY POINTER STRING ## //
	printf(UNDERLINE"\n-Print empty pointer string-\n\n"RESET);
	count = 0;
	printf(GREEN "\nprintf =	%s\n" RESET, pstr);
	ft_printf(CYAN "ft_printf =	");
	count = ft_printf("%s", pstr);
	printf(RESET "\nChars printed > \"%d\"\n", count);
	sleep(1);
*/
/*
// ### PRINT A DECIMAL (base 10) ### ///
	printf(UNDERLINE"\n-Print a decimal (base 10)-\n\n"RESET);

	// ## POSITIVE NUMBERS ## //
	printf(UNDERLINE"\n-Print positive numbers-\n\n"RESET);

	n = 0;
	while (n <= 10)
	{
		count = 0;
		printf(GREEN "\nprintf =	%d\n" RESET, n);
		ft_printf(CYAN "ft_printf =	");
		count = ft_printf("%d", n);
		printf(RESET "\nChars printed > \"%d\"\n", count);
		n++;
	}

	// ## NEGATIVE NUMBERS ## //
	printf(UNDERLINE"\n-Print negative numbers-\n\n"RESET);

	n = -10;
	while (n <= 0)
	{
		count = 0;
		printf(GREEN "\nprintf =	%d\n" RESET, n);
		ft_printf(CYAN "ft_printf =	");
		count = ft_printf("%d", n);
		printf(RESET "\nChars printed > \"%d\"\n", count);
		n++;
	}
	sleep(1);

	count = 0;
	printf(GREEN "\nprintf =	%d\n" RESET, -254863);
	ft_printf(CYAN "ft_printf =	");
	count = ft_printf("%d", -254863);
	printf(RESET "\nChars printed > \"%d\"\n", count);
	n++;
*/
/*
// ### PRINT AN INTEGER in base 10 ### ///
	printf(UNDERLINE"\n-Print an integer in base 10-\n\n"RESET);

	// ## POSITIVE NUMBERS ## //
	printf(UNDERLINE"\n-Print positive numbers-\n\n"RESET);

	n = 0;
	while (n <= 10)
	{
		count = 0;
		printf(GREEN "\nprintf =	%i\n" RESET, n);
		ft_printf(CYAN "ft_printf =	");
		count = ft_printf("%i", n);
		printf(RESET "\nChars printed > \"%d\"\n", count);
		n++;
	}

	// ## NEGATIVE NUMBERS ## //
	printf(UNDERLINE"\n-Print negative numbers-\n\n"RESET);

	n = -10;
	while (n <= 0)
	{
		count = 0;
		printf(GREEN "\nprintf =	%i\n" RESET, n);
		ft_printf(CYAN "ft_printf =	");
		count = ft_printf("%i", n);
		printf(RESET "\nChars printed > \"%d\"\n", count);
		n++;
	}
	sleep(1);

	count = 0;
	printf(GREEN "\nprintf =	%d\n" RESET, -254863);
	ft_printf(CYAN "ft_printf =	");
	count = ft_printf("%d", -254863);
	printf(RESET "\nChars printed > \"%d\"\n", count);
*/
// ### PRINT AN UNSIGNED DECIMAL (base 10) ### ///
	printf(UNDERLINE"\n-Print an unsigned decimal (base 10)-\n\n"RESET);

	// ## POSITIVE NUMBERS ## //
	printf(UNDERLINE"\n-Print positive numbers-\n\n"RESET);

	unsigned_dec = 0;
	while (unsigned_dec <= 10)
	{
		count = 0;
		printf(GREEN "\nprintf =	%i\n" RESET, unsigned_dec);
		ft_printf(CYAN "ft_printf =	");
		count = ft_printf("%i", unsigned_dec);
		printf(RESET "\nChars printed > \"%d\"\n", count);
		unsigned_dec++;
	}

	// ## NEGATIVE NUMBERS ## //
	printf(UNDERLINE"\n-Print negative numbers-\n\n"RESET);

	unsigned_dec = -10;
	while (unsigned_dec <= 0)
	{
		count = 0;
		printf(GREEN "\nprintf =	%u\n" RESET, unsigned_dec);
		ft_printf(CYAN "ft_printf =	");
		count = ft_printf("%u", unsigned_dec);
		printf(RESET "\nChars printed > \"%d\"\n", count);
		unsigned_dec++;
	}
	sleep(1);

	count = 0;
	printf(GREEN "\nprintf =	%u\n" RESET, -254863);
	ft_printf(CYAN "ft_printf =	");
	count = ft_printf("%u", -254863);
	printf(RESET "\nChars printed > \"%d\"\n", count);















	// ;
	// unsigned	int	unsigned_dec_neg = -8;
	// void	*ptr = &n;

/*
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
