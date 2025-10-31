/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   main.c                                             :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: roandrie <roandrie@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/29 09:10:35 by roandrie          #+#    #+#             */
/*   Updated: 2025/10/31 16:47:15 by roandrie         ###   ########.fr       */
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
	char			*str = "Hello!";
	char			*pstr = NULL;
	int				n = 0;
	unsigned	int	unsigned_dec = 0;
	void			*ptr = &n;
	void 			*ptr_v = NULL;

// INT MIN / INT MAX

	ft_printf(RED"\n--- ft_printf test ---\n"RESET);
	printf("\n"RESET);
	sleep (1);

	ft_printf("\nPress something to continue the test\n");
	getchar();

// ### PRINT AN EMPTY PRINT ### ///
	printf(UNDERLINE"\n-Print empty-\n\n"RESET);
	count = ft_printf("");
	printf("\nCount = %d\n", count);

	ft_printf("\nPress something to continue the test\n");
	getchar();

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

	ft_printf("\nPress something to continue the test\n");
	getchar();

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

// ### PRINT AN UNSIGNED DECIMAL (base 10) ### ///
	printf(UNDERLINE"\n-Print an unsigned decimal (base 10)-\n\n"RESET);

	// ## POSITIVE NUMBERS ## //
	printf(UNDERLINE"\n-Print positive numbers-\n\n"RESET);

	unsigned_dec = 0;
	while (unsigned_dec <= 10)
	{
		count = 0;
		printf(GREEN "\nprintf =	%u\n" RESET, unsigned_dec);
		ft_printf(CYAN "ft_printf =	");
		count = ft_printf("%u", unsigned_dec);
		printf(RESET "\nChars printed > \"%d\"\n", count);
		unsigned_dec++;
	}

	count = 0;
	printf(GREEN "\nprintf =	%u\n" RESET, 15870);
	ft_printf(CYAN "ft_printf =	");
	count = ft_printf("%u", 15870);
	printf(RESET "\nChars printed > \"%d\"\n", count);

	count = 0;
	printf(GREEN "\nprintf =	%u\n" RESET, -150);
	ft_printf(CYAN "ft_printf =	");
	count = ft_printf("%u", -150);
	printf(RESET "\nChars printed > \"%d\"\n", count);

// ### PRINT A PERCENT SIGN ### ///
	printf(UNDERLINE"\n-Print a percent sign-\n\n"RESET);

	printf(GREEN"Printf =	%%\n" RESET);
	ft_printf(CYAN "ft_printf =	");
	count = ft_printf("%%");
	printf(RESET "\nChars printed > \"%d\"\n", count);
	sleep(1);

	printf(GREEN"Printf =	%%%%\n"RESET);
	ft_printf(CYAN "ft_printf =	");
	count = ft_printf("%%%%");
	printf(RESET "\nChars printed > \"%d\"\n", count);
	sleep(1);


// ### PRINT A NUMBER IN HEXADECIMAL (base 16) lowercase format ### ///
	printf(UNDERLINE"\n-Print a number in hexadecimal (base 16) lowercase format-\n\n"RESET);

	// ## POSITIVE NUMBERS ## //
	printf(UNDERLINE"\n-Print positive numbers-\n\n"RESET);

	n = 0;
	while (n <= 16)
	{
		count = 0;
		printf(GREEN "\nprintf =	%x\n" RESET, n);
		ft_printf(CYAN "ft_printf =	");
		count = ft_printf("%x", n);
		printf(RESET "\nChars printed > \"%d\"\n", count);
		n++;
	}

	count = 0;
	printf(GREEN "\nprintf =	%x\n" RESET, 42);
	ft_printf(CYAN "ft_printf =	");
	count = ft_printf("%x", 42);
	printf(RESET "\nChars printed > \"%d\"\n", count);

	count = 0;
	printf(GREEN "\nprintf =	%x\n" RESET, 50);
	ft_printf(CYAN "ft_printf =	");
	count = ft_printf("%x", 50);
	printf(RESET "\nChars printed > \"%d\"\n", count);

	count = 0;
	printf(GREEN "\nprintf =	%x\n" RESET, -50);
	ft_printf(CYAN "ft_printf =	");
	count = ft_printf("%x", -50);
	printf(RESET "\nChars printed > \"%d\"\n", count);


// ### PRINT A NUMBER IN HEXADECIMAL (base 16) uppercase format ### ///
	printf(UNDERLINE"\n-Print a number in hexadecimal (base 16) uppercase format-\n\n"RESET);

	// ## POSITIVE NUMBERS ## //
	printf(UNDERLINE"\n-Print positive numbers-\n\n"RESET);

	n = 0;
	while (n <= 16)
	{
		count = 0;
		printf(GREEN "\nprintf =	%X\n" RESET, n);
		ft_printf(CYAN "ft_printf =	");
		count = ft_printf("%X", n);
		printf(RESET "\nChars printed > \"%d\"\n", count);
		n++;
	}

	count = 0;
	printf(GREEN "\nprintf =	%X\n" RESET, 42);
	ft_printf(CYAN "ft_printf =	");
	count = ft_printf("%X", 42);
	printf(RESET "\nChars printed > \"%d\"\n", count);

	count = 0;
	printf(GREEN "\nprintf =	%x\n" RESET, 50);
	ft_printf(CYAN "ft_printf =	");
	count = ft_printf("%X", 50);
	printf(RESET "\nChars printed > \"%d\"\n", count);

	count = 0;
	printf(GREEN "\nprintf =	%X\n" RESET, -50);
	ft_printf(CYAN "ft_printf =	");
	count = ft_printf("%X", -50);
	printf(RESET "\nChars printed > \"%d\"\n", count);

/// ### PRINT THE VOID * POINTER ### ///
	printf(UNDERLINE"\n-Print THE VOID * pointer-\n\n"RESET);

	printf(GREEN "\nprintf =	%p\n" RESET, ptr);
	ft_printf(CYAN "ft_printf =	");
	count = ft_printf("%p", ptr);
	printf(RESET "\nChars printed > \"%d\"\n", count);

	printf(GREEN "\nprintf =	%p\n" RESET, &ptr);
	ft_printf(CYAN "ft_printf =	");
	count = ft_printf("%p", &ptr);
	printf(RESET "\nChars printed > \"%d\"\n", count);

	printf(GREEN "\nprintf =	%p\n" RESET, ptr_v);
	ft_printf(CYAN "ft_printf =	");
	count = ft_printf("%p", ptr_v);
	printf(RESET "\nChars printed > \"%d\"\n", count);


}
