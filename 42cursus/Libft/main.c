/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   main.c                                             :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: roandrie <roandrie@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/18 14:35:15 by roandrie          #+#    #+#             */
/*   Updated: 2025/10/23 13:07:34 by roandrie         ###   ########.fr       */
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

/*
#include <stdio.h>
int main()
{
	char str[] = "bonjour";
	t_list	*new;
	new = ft_lstnew(str);
	printf("%c\n", *(char *)new->content);
	free (new);
}
*/

void	show_menu(int menu_showed)
{
	if (menu_showed == 1)
		system("clear");
	printf(CYAN "\n============== MENU ==============\n" RESET);
	printf("   " UNDERLINE "Choose the function to test:\n\n" RESET);
	printf("1.	ft_isalpha	14.	ft_tolower	27.	ft_split\n");
	printf("2.	ft_isdigit	15.	ft_strchr	28.	ft_itoa\n");
	printf("3.	ft_isalnum	16.	ft_strrchr	29.	ft_strmapi\n");
	printf("4.	ft_isascii	17.	ft_strncmp	30.	ft_striteri\n");
	printf("5.	ft_isprint	18.	ft_memchr	31.	ft_putchar_fd\n");
	printf("6.	ft_strlen	19.	ft_memcmp	32.	ft_putstr_fd\n");
	printf("7.	ft_memset	20.	ft_strnstr	33.	ft_putendl_fd\n");
	printf("8.	ft_bzero	21.	ft_atoi		34.	ft_putnbr_fd\n");
	printf("9.	ft_memcpy	22.	ft_calloc\n");
	printf("10.	ft_memmove	23.	ft_strdup\n");
	printf("11.	ft_strlcpy	24.	ft_substr\n");
	printf("12.	ft_strlcat	25.	ft_strjoin\n");
	printf("13.	ft_toupper	26.	ft_strtrim\n");
	printf("\n\n0. Leave\n");
	printf(CYAN "\n====================================\n" RESET);
}

// == Test programs ==

void test_ft_isalpha()
{
	char	c;
	int		result;

	printf(UNDERLINE"\n=========="RESET"Testing "RED"ft_isalpha" RESET UNDERLINE "==========\n" RESET);
	printf("\nInstruction (1/1) : write a character to perfom the test\n");
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
	printf("\nInstruction (1/1) : write a number (0 to 9) to perfom the test\n");
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
	printf("\nInstruction (1/1) : write a number or a letter to perfom the test\n");
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
	printf("\nInstruction (1/1) : write an ASCII character to perfom the test\n");
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
	printf("\nInstruction (1/1) : write a printable character to perfom the test\n");
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
	printf("\nInstruction (1/1) : write a string to perfom the test\n");
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

void test_ft_memset()
{
	char	str[100];
	char	str_copy[100];
	char	str_buffer[10];
	int		c;
	size_t	n;

	memset(str, 0, 100);
	memset(str_copy, 0, 100);
	printf(UNDERLINE"\n=========="RESET"Testing "RED"ft_memset" RESET UNDERLINE "==========\n" RESET);
	printf("\nInstruction (1/3) : write a string\n");
	fgets(str, sizeof(str), stdin);
	str[strcspn(str, "\n")] = 0;
	strcpy(str_copy, str);
	printf("\nInstruction (2/3) : write the character you want to fill the string with\n");
	fgets(str_buffer, sizeof(str_buffer), stdin);
	c = str_buffer[0];
	printf("\nInstruction (3/3) : give the numbers of octets you want\n");
	scanf("%zu", &n);
	getchar();
	printf("\n/!\\ Testing in progress /!\\\n\n");
	ft_memset(str, c, n);
	memset(str_copy, c, n);
	sleep((1));
	if (memcmp(str, str_copy, 100) == 0)
	{
		printf(GREEN "[SUCCESS]\n");
		printf(RESET);
	}
	else
	{
		printf(RED "[FAILED]\n");
		printf(RESET);
	}
	sleep(2);
}

void test_ft_bzero()
{
	char	str[100];
	char	str_copy[100];
	size_t	n;

	memset(str, 0, 100);
	memset(str_copy, 0, 100);
	printf(UNDERLINE"\n=========="RESET"Testing "RED"ft_bzero" RESET UNDERLINE "==========\n" RESET);
	printf("\nInstruction (1/2) : write a string\n");
	fgets(str, sizeof(str), stdin);
	str[strcspn(str, "\n")] = 0;
	strcpy(str_copy, str);
	printf("\nInstruction (2/2) : give the numbers of octets you want\n");
	scanf("%zu", &n);
	getchar();
	printf("\n/!\\ Testing in progress /!\\\n\n");
	ft_bzero(str, n);
	memset(str_copy, 0, n);
	sleep((1));
	if (memcmp(str, str_copy, 100) == 0)
	{
		printf(GREEN "[SUCCESS]\n");
		printf(RESET);
	}
	else
	{
		printf(RED "[FAILED]\n");
		printf(RESET);
	}
	sleep(2);
}
void test_ft_memcpy()
{
	char	str[100];
	char	dest[100];
	char	dest_copy[100];
	char	dest_original[100];
	char	*result;
	size_t	n;

	memset(str, 0, 100);
	memset(dest, 0, 100);
	memset(dest_copy, 0, 100);
	memset(dest_original, 0, 100);
	printf(UNDERLINE"\n=========="RESET"Testing "RED"ft_memcpy" RESET UNDERLINE "==========\n" RESET);
	printf("\nInstruction (1/3) : write a string (destination)\n");
	fgets(dest, sizeof(dest), stdin);
	dest[strcspn(dest, "\n")] = 0;
	strcpy(dest_copy, dest);
	strcpy(dest_original, dest);
	printf("\nInstruction (2/3) : write a string (source)\n");
	fgets(str, sizeof(str), stdin);
	str[strcspn(str, "\n")] = 0;
	printf("\nInstruction (3/3) : write the numbers of octets you want\n");
	scanf("%zu", &n);
	getchar();
	printf("\n/!\\ Testing in progress /!\\\n\n");
	result = ft_memcpy(dest, str, n);
	memcpy(dest_copy, str, n);
	sleep((1));
	if (memcmp(dest, dest_copy, 100) == 0 && result == dest)
	{
		printf(GREEN "[SUCCESS]\n");
		printf("Original string	=	%s\n", dest_original);
		printf("New	string	=	%s\n", dest);
		printf(RESET);
	}
	else
	{
		printf(RED "[FAILED]\n");
		if (memcmp(dest, dest_copy, 100) != 0)
		{
			printf("[Mismatch]\n");
			printf("ft_memcpy:	%s\n", dest);
			printf("memcpy   :	%s\n", dest_copy);
		}
		if (result != dest)
			printf("Incorrect Pointer or NULL\n");
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
		else if (choice == 7)
			test_ft_memset();
		else if (choice == 8)
			test_ft_bzero();
		else if (choice == 9)
			test_ft_memcpy();
		else if (choice == 0)
			printf("Goodbye!\n");
		else
			printf(RED "Invalid number. Please, put a number that exist in the list.");
		if (choice != 0 && choice >= 1 && choice <= 9)
		{
			printf("\n(Press Enter to return to the menu)");
			getchar();
		}
	}
	return (0);
}
