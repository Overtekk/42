/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   main.c                                             :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: roandrie <roandrie@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/29 09:10:35 by roandrie          #+#    #+#             */
/*   Updated: 2025/11/03 10:55:19 by roandrie         ###   ########.fr       */
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
	int				n = 0;
	unsigned int	unsigned_dec = 0;
	char			*pstr = NULL;
	void			*ptr = &n;
	void 			*ptr_v = NULL;

// ## TEST ## //
	ft_printf(RED UNDERLINE"\n--- ft_printf test ---\n"RESET);
	sleep (1);

	//
	ft_printf("\nPress enter to continue the test\n");
	getchar();
	sleep(1);
	//

// ### PRINT AN EMPTY PRINT ### ///
	ft_printf(RED UNDERLINE"\n	-Print empty-\n\n"RESET);

	count = ft_printf("");
	ft_printf("\nCount = %d\n", count);

	//
	ft_printf("\nPress enter to continue the test\n");
	getchar();
	sleep(1);
	//

// ### PRINT CHARACTER ### ///
	ft_printf(RED UNDERLINE"\n	-Print a character-\n\n"RESET);

	while (c <= 'g')
	{
		count = 0;
		printf(GREEN "\nprintf =	%c\n" RESET, c);
		ft_printf(CYAN "ft_printf =	");
		count = ft_printf("%c", c);
		ft_printf(RESET "\nChars printed > \"%d\"\n", count);
		c++;
	}
	sleep(1);

	//
	ft_printf("\nPress enter to continue the test\n");
	getchar();
	sleep(1);
	//

// ### PRINT A STRING ### ///
	ft_printf(RED UNDERLINE"\n	-Print a string-\n\n"RESET);

	// ## NORMAL STRING ## //
	ft_printf(UNDERLINE"\n-Print normal string-\n\n"RESET);

	count = 0;
	printf(GREEN "\nprintf =	%s\n" RESET, str);
	ft_printf(CYAN "ft_printf =	");
	count = ft_printf("%s", str);
	ft_printf(RESET "\nChars printed > \"%d\"\n", count);
	sleep(1);

	// ## EMPTY STRING ## //
	ft_printf(UNDERLINE"\n-Print empty string-\n\n"RESET);

	count = 0;
	printf(GREEN "\nprintf =	%s\n" RESET, "");
	ft_printf(CYAN "ft_printf =	");
	count = ft_printf("%s", "");
	ft_printf(RESET "\nChars printed > \"%d\"\n", count);
	sleep(1);

	// ## EMPTY POINTER STRING ## //
	ft_printf(UNDERLINE"\n-Print empty pointer string-\n\n"RESET);

	count = 0;
	printf(GREEN "\nprintf =	%s\n" RESET, pstr);
	ft_printf(CYAN "ft_printf =	");
	count = ft_printf("%s", pstr);
	ft_printf(RESET "\nChars printed > \"%d\"\n", count);
	sleep(1);

	//
	ft_printf("\nPress enter to continue the test\n");
	getchar();
	sleep(1);
	//

// ### PRINT A DECIMAL (base 10) ### ///
	ft_printf(RED UNDERLINE"\n	-Print a decimal (base 10)-\n\n"RESET);

	// ## POSITIVE NUMBERS ## //
	ft_printf(UNDERLINE"\n-Print positive numbers-\n\n"RESET);

	n = 0;
	while (n <= 10)
	{
		count = 0;
		printf(GREEN "\nprintf =	%d\n" RESET, n);
		ft_printf(CYAN "ft_printf =	");
		count = ft_printf("%d", n);
		ft_printf(RESET "\nChars printed > \"%d\"\n", count);
		n++;
	}
	sleep(2);

	// ## NEGATIVE NUMBERS ## //
	printf(UNDERLINE"\n-Print negative numbers-\n\n"RESET);

	n = -10;
	while (n <= 0)
	{
		count = 0;
		printf(GREEN "\nprintf =	%d\n" RESET, n);
		ft_printf(CYAN "ft_printf =	");
		count = ft_printf("%d", n);
		ft_printf(RESET "\nChars printed > \"%d\"\n", count);
		n++;
	}
	sleep(2);

	// ## BIG NUMBER ## //
	ft_printf(UNDERLINE"\n-Print big number-\n\n"RESET);

	count = 0;
	printf(GREEN "\nprintf =	%d\n" RESET, -254863);
	ft_printf(CYAN "ft_printf =	");
	count = ft_printf("%d", -254863);
	ft_printf(RESET "\nChars printed > \"%d\"\n", count);
	sleep(1);

	// ## INT MAX / MIN ## //
	ft_printf(UNDERLINE"\n-Print int max && min-\n\n"RESET);

	count = 0;
	printf(GREEN "\nprintf =	%d\n" RESET, INT_MAX);
	ft_printf(CYAN "ft_printf =	");
	count = ft_printf("%d", INT_MAX);
	ft_printf(RESET "\nChars printed > \"%d\"\n", count);
	sleep(1);

	count = 0;
	printf(GREEN "\nprintf =	%d\n" RESET, INT_MIN);
	ft_printf(CYAN "ft_printf =	");
	count = ft_printf("%d", INT_MIN);
	ft_printf(RESET "\nChars printed > \"%d\"\n", count);
	sleep(1);

	//
	ft_printf("\nPress enter to continue the test\n");
	getchar();
	sleep(1);
	//


// ### PRINT AN INTEGER in base 10 ### ///
	ft_printf(RED UNDERLINE"\n	-Print an integer in base 10-\n\n"RESET);

	// ## POSITIVE NUMBERS ## //
	ft_printf(UNDERLINE"\n-Print positive numbers-\n\n"RESET);

	n = 0;
	while (n <= 10)
	{
		count = 0;
		printf(GREEN "\nprintf =	%i\n" RESET, n);
		ft_printf(CYAN "ft_printf =	");
		count = ft_printf("%i", n);
		ft_printf(RESET "\nChars printed > \"%d\"\n", count);
		n++;
	}
	sleep (2);

	// ## NEGATIVE NUMBERS ## //
	ft_printf(UNDERLINE"\n-Print negative numbers-\n\n"RESET);

	n = -10;
	while (n <= 0)
	{
		count = 0;
		printf(GREEN "\nprintf =	%i\n" RESET, n);
		ft_printf(CYAN "ft_printf =	");
		count = ft_printf("%i", n);
		ft_printf(RESET "\nChars printed > \"%d\"\n", count);
		n++;
	}
	sleep(2);

	// ## BIG NUMBER ## //
	ft_printf(UNDERLINE"\n-Print big number-\n\n"RESET);

	count = 0;
	printf(GREEN "\nprintf =	%d\n" RESET, -254863);
	ft_printf(CYAN "ft_printf =	");
	count = ft_printf("%d", -254863);
	ft_printf(RESET "\nChars printed > \"%d\"\n", count);
	sleep(1);

	// ## INT MAX / MIN ## //
	ft_printf(UNDERLINE"\n-Print int max && min-\n\n"RESET);

	count = 0;
	printf(GREEN "\nprintf =	%d\n" RESET, INT_MAX);
	ft_printf(CYAN "ft_printf =	");
	count = ft_printf("%d", INT_MAX);
	ft_printf(RESET "\nChars printed > \"%d\"\n", count);
	sleep(1);

	count = 0;
	printf(GREEN "\nprintf =	%d\n" RESET, INT_MIN);
	ft_printf(CYAN "ft_printf =	");
	count = ft_printf("%d", INT_MIN);
	ft_printf(RESET "\nChars printed > \"%d\"\n", count);
	sleep(1);

	//
	ft_printf("\nPress enter to continue the test\n");
	getchar();
	sleep(1);
	//

// ### PRINT AN UNSIGNED DECIMAL (base 10) ### ///
	ft_printf(RED UNDERLINE"\n	-Print an unsigned decimal (base 10)-\n\n"RESET);

	// ## POSITIVE NUMBERS ## //
	ft_printf(UNDERLINE"\n-Print positive numbers-\n\n"RESET);

	unsigned_dec = 0;
	while (unsigned_dec <= 10)
	{
		count = 0;
		printf(GREEN "\nprintf =	%u\n" RESET, unsigned_dec);
		ft_printf(CYAN "ft_printf =	");
		count = ft_printf("%u", unsigned_dec);
		ft_printf(RESET "\nChars printed > \"%d\"\n", count);
		unsigned_dec++;
	}
	sleep (2);

	// ## BIG NUMBER ## //
	ft_printf(UNDERLINE"\n-Print big number-\n\n"RESET);

	count = 0;
	printf(GREEN "\nprintf =	%u\n" RESET, 15870);
	ft_printf(CYAN "ft_printf =	");
	count = ft_printf("%u", 15870);
	ft_printf(RESET "\nChars printed > \"%d\"\n", count);
	sleep(1);

	// ## NEGATIVE NUMBER ## //
	ft_printf(UNDERLINE"\n-Print negative number-\n\n"RESET);

	count = 0;
	printf(GREEN "\nprintf =	%u\n" RESET, -150);
	ft_printf(CYAN "ft_printf =	");
	count = ft_printf("%u", -150);
	ft_printf(RESET "\nChars printed > \"%d\"\n", count);
	sleep(1);

	// ## INT MAX - MIN ## //
	ft_printf(UNDERLINE"\n-Print int max && int min-\n\n"RESET);

	count = 0;
	printf(GREEN "\nprintf =	%u\n" RESET, INT_MAX);
	ft_printf(CYAN "ft_printf =	");
	count = ft_printf("%u", INT_MAX);
	ft_printf(RESET "\nChars printed > \"%d\"\n", count);
	sleep(1);

	count = 0;
	printf(GREEN "\nprintf =	%u\n" RESET, INT_MIN);
	ft_printf(CYAN "ft_printf =	");
	count = ft_printf("%u", INT_MIN);
	ft_printf(RESET "\nChars printed > \"%d\"\n", count);
	sleep(1);

	//
	ft_printf("\nPress enter to continue the test\n");
	getchar();
	sleep(1);
	//

// ### PRINT A PERCENT SIGN ### ///
	ft_printf(RED UNDERLINE"\n	-Print a percent sign-\n\n"RESET);

	printf(GREEN"Printf =	%%\n" RESET);
	ft_printf(CYAN "ft_printf =	");
	count = ft_printf("%%");
	ft_printf(RESET "\nChars printed > \"%d\"\n\n", count);
	sleep(1);

	printf(GREEN"Printf =	%%%%\n"RESET);
	ft_printf(CYAN "ft_printf =	");
	count = ft_printf("%%%%");
	ft_printf(RESET "\nChars printed > \"%d\"\n", count);
	sleep(1);

	//
	ft_printf("\nPress enter to continue the test\n");
	getchar();
	sleep(1);
	//

// ### PRINT A NUMBER IN HEXADECIMAL (base 16) lowercase format ### ///
	ft_printf(RED UNDERLINE"\n	-Print a number in hexadecimal (base 16) lowercase format-\n\n"RESET);

	// ## POSITIVE NUMBERS ## //
	ft_printf(UNDERLINE"\n-Print positive numbers-\n\n"RESET);

	n = 0;
	while (n <= 16)
	{
		count = 0;
		printf(GREEN "\nprintf =	%x\n" RESET, n);
		ft_printf(CYAN "ft_printf =	");
		count = ft_printf("%x", n);
		ft_printf(RESET "\nChars printed > \"%d\"\n", count);
		n++;
	}
	sleep (2);

	// ## OTHER NUMBER ## //
	ft_printf(UNDERLINE"\n-Print other number-\n\n"RESET);

	count = 0;
	printf(GREEN "\nprintf =	%x\n" RESET, 42);
	ft_printf(CYAN "ft_printf =	");
	count = ft_printf("%x", 42);
	ft_printf(RESET "\nChars printed > \"%d\"\n", count);
	sleep (1);

	// ## NEGATVE NUMBER ## //
	ft_printf(UNDERLINE"\n-Print negative number-\n\n"RESET);

	count = 0;
	printf(GREEN "\nprintf =	%x\n" RESET, 50);
	ft_printf(CYAN "ft_printf =	");
	count = ft_printf("%x", 50);
	ft_printf(RESET "\nChars printed > \"%d\"\n", count);
	sleep (1);

	// ## INT MAX - MIN ## //
	ft_printf(UNDERLINE"\n-Print int max && min-\n\n"RESET);

	count = 0;
	printf(GREEN "\nprintf =	%x\n" RESET, INT_MAX);
	ft_printf(CYAN "ft_printf =	");
	count = ft_printf("%x", INT_MAX);
	ft_printf(RESET "\nChars printed > \"%d\"\n", count);
	sleep (1);

	count = 0;
	printf(GREEN "\nprintf =	%x\n" RESET, INT_MIN);
	ft_printf(CYAN "ft_printf =	");
	count = ft_printf("%x", INT_MIN);
	ft_printf(RESET "\nChars printed > \"%d\"\n", count);
	sleep (1);

	//
	ft_printf("\nPress enter to continue the test\n");
	getchar();
	sleep(1);
	//

// ### PRINT A NUMBER IN HEXADECIMAL (base 16) uppercase format ### ///
	ft_printf(RED UNDERLINE"\n	-Print a number in hexadecimal (base 16) uppercase format-\n\n"RESET);

	// ## POSITIVE NUMBERS ## //
	ft_printf(UNDERLINE"\n-Print positive numbers-\n\n"RESET);

	n = 0;
	while (n <= 16)
	{
		count = 0;
		printf(GREEN "\nprintf =	%X\n" RESET, n);
		ft_printf(CYAN "ft_printf =	");
		count = ft_printf("%X", n);
		ft_printf(RESET "\nChars printed > \"%d\"\n", count);
		n++;
	}
	sleep (2);

	// ## OTHER NUMBER ## //
	ft_printf(UNDERLINE"\n-Print other number-\n\n"RESET);

	count = 0;
	printf(GREEN "\nprintf =	%X\n" RESET, 82);
	ft_printf(CYAN "ft_printf =	");
	count = ft_printf("%X", 82);
	ft_printf(RESET "\nChars printed > \"%d\"\n", count);
	sleep (1);

	// ## NEGATVE NUMBER ## //
	ft_printf(UNDERLINE"\n-Print negative number-\n\n"RESET);

	count = 0;
	printf(GREEN "\nprintf =	%X\n" RESET, -50);
	ft_printf(CYAN "ft_printf =	");
	count = ft_printf("%X", -50);
	ft_printf(RESET "\nChars printed > \"%d\"\n", count);
	sleep (1);

	// ## INT MAX - MIN ## //
	ft_printf(UNDERLINE"\n-Print int max && min-\n\n"RESET);

	count = 0;
	printf(GREEN "\nprintf =	%X\n" RESET, INT_MAX);
	ft_printf(CYAN "ft_printf =	");
	count = ft_printf("%X", INT_MAX);
	ft_printf(RESET "\nChars printed > \"%d\"\n", count);
	sleep (1);

	count = 0;
	printf(GREEN "\nprintf =	%X\n" RESET, INT_MIN);
	ft_printf(CYAN "ft_printf =	");
	count = ft_printf("%X", INT_MIN);
	ft_printf(RESET "\nChars printed > \"%d\"\n", count);
	sleep (1);

	//
	ft_printf("\nPress enter to continue the test\n");
	getchar();
	sleep(1);
	//

/// ### PRINT THE VOID * POINTER ### ///
	ft_printf(RED UNDERLINE"\n	-Print THE VOID * pointer-\n\n"RESET);

	// ## POINTER ## //
	ft_printf(UNDERLINE"\n-Print a pointer-\n\n"RESET);

	count = 0;
	printf(GREEN "\nprintf =	%p\n" RESET, ptr);
	ft_printf(CYAN "ft_printf =	");
	count = ft_printf("%p", ptr);
	ft_printf(RESET "\nChars printed > \"%d\"\n", count);
	sleep(1);

	// ## ADRESS ## //
	ft_printf(UNDERLINE"\n-Print an adress-\n\n"RESET);

	count = 0;
	printf(GREEN "\nprintf =	%p\n" RESET, &ptr);
	ft_printf(CYAN "ft_printf =	");
	count = ft_printf("%p", &ptr);
	ft_printf(RESET "\nChars printed > \"%d\"\n", count);
	sleep(1);

	// ## NULL ## //
	ft_printf(UNDERLINE"\n-Print NULL pointer-\n\n"RESET);

	count = 0;
	printf(GREEN "\nprintf =	%p\n" RESET, ptr_v);
	ft_printf(CYAN "ft_printf =	");
	count = ft_printf("%p", ptr_v);
	ft_printf(RESET "\nChars printed > \"%d\"\n", count);
	sleep(1);

	//
	ft_printf("\nPress enter to continue the test\n");
	getchar();
	sleep(1);
	//

/// ### TEST OTHER CONVERSION ### ///
	ft_printf(RED UNDERLINE"\n	-Test other conversion-\n\n"RESET);

	count = 0;
	printf(GREEN "\nprintf =	%f\n" RESET, 0.21);
	ft_printf(CYAN "ft_printf =	");
	count = ft_printf("%f", 0.21);
	ft_printf(RESET "\nChars printed > \"%d\"\n", count);
	sleep(2);

/// ### PRINT ALL CONVERSIONS ### ///
	ft_printf(RED UNDERLINE"\n	-Print all conversions-\n\n"RESET);

	count = 0;
	count = printf(GREEN"\nprintf =	%c, %s, %p, %d, %i, %u, %x, %X, %%\n" RESET, 'a', "Hey!", ptr, 12, 48, 63, 89, 145);
	ft_printf(CYAN "ft_printf =	");
	count = ft_printf("%c, %s, %p, %d, %i, %u, %x, %X, %%", 'a', "Hey!", ptr, 12, 48, 63, 89, 145);
	ft_printf(RESET "\nChars printed > \"%d\"\n", count);
	sleep(2);

	ft_printf(UNDERLINE"\n-END OF TESTS-\n\n"RESET);

	return (0);
}
