/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   main.c                                             :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: roandrie <roandrie@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/18 14:35:15 by roandrie          #+#    #+#             */
/*   Updated: 2025/10/21 21:06:24 by roandrie         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"
#include <stdio.h>

#define	RESET		"\033[0m"
#define	UNDERLINE	"\033[4m"
#define	RED			"\033[31m"
#define	GREEN		"\033[32m"
#define	YELLOW		"\033[33m"
#define	BLUE		"\033[34m"
#define	PURPLE		"\033[35m"
#define	CYAN		"\033[36m"

void	show_menu(int menu_showed)
{
	if (menu_showed == 1)
		system("clear");
	printf(CYAN "\n============== MENU ==============\n" RESET);
	printf("   " UNDERLINE "Choose the function to test:\n\n" RESET);
	printf("1. ft_isalpha\n");
	printf("2. ft_isdigit\n");
	printf("3. ft_isalnum\n");
	printf("4. ft_isascii\n");
	printf("5. ft_isprint\n");
	printf("6. ft_strlen\n");
	printf("\n");
	printf("0. Leave\n");
	printf(CYAN "\n====================================\n" RESET);
}

// == Test programs ==

void test_ft_isalpha()
{
	char	c;
	int		result;

	printf(UNDERLINE"\n=========="RESET"Testing "RED"ft_isalpha" RESET UNDERLINE "==========\n" RESET);
	printf("\nInstruction : put a character to perfom the test\n");
	scanf(" %c", &c);
	printf("\n/!\\ Testing in progress /!\\\n\n");
	result = ft_isalpha(c);
	getchar();
	sleep((1));
	if (result >= 1)
	{
		printf(GREEN "[SUCCESS] %c is alpha\n", c);
		printf(RESET);
	}
	else
	{
		printf(RED "[FAILED] %c is not alpha\n", c);
		printf(RESET);
	}
	sleep(2);
}

void test_ft_isdigit()
{
	char	c;
	int		result;

	printf(UNDERLINE"\n=========="RESET"Testing "RED"ft_isdigit" RESET UNDERLINE "==========\n" RESET);
	printf("\nInstruction : put a number (0 to 9) to perfom the test\n");
	scanf(" %c", &c);
	printf("\n/!\\ Testing in progress /!\\\n\n");
	result = ft_isdigit(c);
	getchar();
	sleep((1));
	if (result >= 1)
	{
		printf(GREEN "[SUCCESS] %c is a digit\n", c);
		printf(RESET);
	}
	else
	{
		printf(RED "[FAILED] %c is not a digit\n", c);
		printf(RESET);
	}
	sleep(2);
}

void test_ft_isalnum()
{
	char	c;
	int		result;

	printf(UNDERLINE"\n=========="RESET"Testing "RED"ft_isalnum" RESET UNDERLINE "==========\n" RESET);
	printf("\nInstruction : put a number or a letter to perfom the test\n");
	scanf(" %c", &c);
	printf("\n/!\\ Testing in progress /!\\\n\n");
	result = ft_isalnum(c);
	getchar();
	sleep((1));
	if (result >= 1)
	{
		printf(GREEN "[SUCCESS] %c is an alphanumeric character\n", c);
		printf(RESET);
	}
	else
	{
		printf(RED "[FAILED] %c is not an alphanumeric character\n", c);
		printf(RESET);
	}
	sleep(2);
}

void test_ft_isascii()
{
	char	c;
	int		result;

	printf(UNDERLINE"\n=========="RESET"Testing "RED"ft_isascii" RESET UNDERLINE "==========\n" RESET);
	printf("\nInstruction : put an ASCII character to perfom the test\n");
	scanf(" %c", &c);
	printf("\n/!\\ Testing in progress /!\\\n\n");
	result = ft_isascii(c);
	getchar();
	sleep((1));
	if (result >= 1)
	{
		printf(GREEN "[SUCCESS] %c is ASCII\n", c);
		printf(RESET);
	}
	else
	{
		printf(RED "[FAILED] %c is not ASCII\n", c);
		printf(RESET);
	}
	sleep(2);
}

void test_ft_isprint()
{
	char	c;
	int		result;

	printf(UNDERLINE"\n=========="RESET"Testing "RED"ft_isprint" RESET UNDERLINE "==========\n" RESET);
	printf("\nInstruction : put a printable character to perfom the test\n");
	scanf(" %c", &c);
	printf("\n/!\\ Testing in progress /!\\\n\n");
	result = ft_isprint(c);
	getchar();
	sleep((1));
	if (result >= 1)
	{
		printf(GREEN "[SUCCESS] %c is printable\n", c);
		printf(RESET);
	}
	else
	{
		printf(RED "[FAILED] %c is not printable\n", c);
		printf(RESET);
	}
	sleep(2);
}
void test_ft_strlen()
{
	char	str[1000];
	int		result, result_comp;

	printf(UNDERLINE"\n=========="RESET"Testing "RED"ft_strlen" RESET UNDERLINE "==========\n" RESET);
	printf("\nInstruction : put a string to perfom the test\n");
	fgets(str, sizeof(str), stdin);
	str[strcspn(str, "\n")] = 0;
	printf("\n/!\\ Testing in progress /!\\\n\n");
	result = ft_strlen(str);
	result_comp = strlen(str);
	sleep((1));
	if (result == result_comp)
	{
		printf(GREEN "[SUCCESS] There are %d characters\n", result);
		printf(RESET);
	}
	else
	{
		printf(RED "[FAILED] There are %c characters\n", result_comp);
		printf(RESET);
	}
	sleep(2);
}

int	main()
{
	int	choice = -1;

	system("clear");
	printf(UNDERLINE "\n--- Libft test---\n" RESET);
	while (choice != 0)
	{
		if (choice == -1)
			show_menu(0);
		else
			show_menu(1);
		scanf("%d", &choice);
		getchar();

		if (choice == 1)
			test_ft_isalpha();
		else if (choice == 2)
			test_ft_isdigit();
		else if (choice == 3)
			test_ft_isalnum();
		else if (choice == 4)
			test_ft_isascii();
		else if (choice == 5)
			test_ft_isprint();
		else if (choice == 6)
			test_ft_strlen();
		else if (choice == 0)
			printf("Goodbye!\n");
		else
			printf(RED "Invalid number. Please, put a number that exist in the list.");
		if (choice != 0 && choice >= 1 && choice <= 6)
		{
			printf("\n(Press Enter to return to the menu)");
			getchar();
		}
	}
	return (0);
}
