/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   main.c                                             :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: roandrie <roandrie@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/18 14:35:15 by roandrie          #+#    #+#             */
/*   Updated: 2025/10/27 10:08:40 by roandrie         ###   ########.fr       */
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

// Function for ft_strmapi
static	char	ft_map_strmapi(unsigned int i, char c)
{
	(void)i;
	if (c >= 'a' && c <= 'z')
		return (ft_toupper(c));
	else if (c >= 'A' && c <= 'Z')
		return (ft_tolower(c));
	return (c);
}
// Function for ft_striteri
static	void	ft_map_striteri(unsigned int i, char *c)
{
	(void)i;
	if (*c != '\0')
		(*c)++;
}
// Function for ft_lstiter
static	void	ft_map_lstiter(void *content)
{
	char	*str;
	int		i;

	str = (char *)content;
	i = 0;
	while (str[i] != '\0')
	{
		if (str[i] == 'o' || str[i] == 'O')
			str[i] = '0';
		else if (str[i] == 'a' || str[i] == 'A')
			str[i] = '4';
		else if (str[i] == 'x' || str[i] == 'X')
			str[i] = '3';
		i++;
	}
}
// Function for ft_lstmap
static	void	*ft_map_lstmap(void *content)
{
	char	*original_str;
	char	*new_str;
	size_t	len;
	size_t	i;

	original_str = (char *)content;
	len = strlen(original_str);
	new_str = malloc(sizeof(char) * (len + 1));
	if (new_str == NULL)
		return (NULL);
	i = 0;
	while (i < len)
	{
		if (i % 2 == 0)
			new_str[i] = '0';
		else
			new_str[i] = '1';
		i++;
	}
	new_str[i] = '\0';
	return ((void *)new_str);
}
// Functions for the bonus part
static	void	print_list(t_list *lst)
{
	t_list *current = lst;
	while (current)
	{
		printf("%s\n", (char *)current->content);
		current = current->next;
	}
}
static	void	ft_del(void *content)
{
	free(content);
}

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
	printf("13.	ft_toupper	26.	ft_strtrim\n\n");
	printf("			-----Bonus part-----\n\n");
	printf("35.	ft_lstnew	36. ft_lstadd_front	37. ft_lstsize\n");
	printf("38.	ft_lstlast	39. ft_lstadd_back	40. ft_lstdelone\n");
	printf("41.	ft_lstclear	42. ft_lstiter		43. ft_lstmap\n");
	printf("\n\n0. Leave\n");
	printf(CYAN "\n====================================\n" RESET);
}

// == Test programs ==

void test_ft_isalpha()
{
	char	c;
	int		result;
	int		choice;

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
	sleep(1);
	printf("\nTap 1 to make another test or 2 to return to main menu\n");
	choice = 0;
	scanf("%d", &choice);
	getchar();
	if (choice == 1)
	{
		test_ft_isalpha();
	}
}

void test_ft_isdigit()
{
	char	c;
	int		result;
	int		choice;

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
	sleep(1);
	printf("\nTap 1 to make another test or 2 to return to main menu\n");
	choice = 0;
	scanf("%d", &choice);
	getchar();
	if (choice == 1)
	{
		test_ft_isdigit();
	}
}

void test_ft_isalnum()
{
	char	c;
	int		result;
	int		choice;

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
	sleep(1);
	printf("\nTap 1 to make another test or 2 to return to main menu\n");
	choice = 0;
	scanf("%d", &choice);
	getchar();
	if (choice == 1)
	{
		test_ft_isalnum();
	}
}

void test_ft_isascii()
{
	char	c;
	int		result;
	int		choice;

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
	sleep(1);
	printf("\nTap 1 to make another test or 2 to return to main menu\n");
	choice = 0;
	scanf("%d", &choice);
	getchar();
	if (choice == 1)
	{
		test_ft_isascii();
	}
}

void test_ft_isprint()
{
	char	c;
	int		result;
	int		choice;

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
	sleep(1);
	printf("\nTap 1 to make another test or 2 to return to main menu\n");
	choice = 0;
	scanf("%d", &choice);
	getchar();
	if (choice == 1)
	{
		test_ft_isprint();
	}
}
void test_ft_strlen()
{
	char	str[1000];
	int		result, result_comp;
	int		choice;

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
	sleep(1);
	printf("\nTap 1 to make another test or 2 to return to main menu\n");
	choice = 0;
	scanf("%d", &choice);
	getchar();
	if (choice == 1)
	{
		test_ft_strlen();
	}
}

void test_ft_memset()
{
	char	str[100];
	char	str_copy[100];
	char	str_buffer[10];
	int		c;
	size_t	n;
	int		choice;

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
	sleep(1);
	printf("\nTap 1 to make another test or 2 to return to main menu\n");
	choice = 0;
	scanf("%d", &choice);
	getchar();
	if (choice == 1)
	{
		test_ft_memset();
	}
}

void test_ft_bzero()
{
	char	str[100];
	char	str_copy[100];
	size_t	n;
	int		choice;

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
	sleep(1);
	printf("\nTap 1 to make another test or 2 to return to main menu\n");
	choice = 0;
	scanf("%d", &choice);
	getchar();
	if (choice == 1)
	{
		test_ft_bzero();
	}
}
void test_ft_memcpy()
{
	char	str[100];
	char	dest[100];
	char	dest_copy[100];
	char	dest_original[100];
	char	*result;
	size_t	n;
	int		choice;

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
			printf(RED "[Mismatch]\n");
			printf("ft_memcpy:	%s\n", dest);
			printf("memcpy   :	%s\n", dest_copy);
		}
		if (result != dest)
		{
			printf(RED "[FAILED]\n");
			printf("Incorrect Pointer or NULL\n");
		}
		printf(RESET);
	}
	sleep(1);
	printf("\nTap 1 to make another test or 2 to return to main menu\n");
	choice = 0;
	scanf("%d", &choice);
	getchar();
	if (choice == 1)
	{
		test_ft_memcpy();
	}
}

void test_ft_memmove()
{
	char	src[100];
	char	dest[100];
	char	dest_copy[100];
	char	dest_original[100];
	char	*result;
	size_t	n;
	int		choice;

	memset(src, 0, 100);
	memset(dest, 0, 100);
	memset(dest_copy, 0, 100);
	memset(dest_original, 0, 100);
	printf(UNDERLINE"\n=========="RESET"Testing "RED"ft_memmemove" RESET UNDERLINE "==========\n" RESET);
	printf("\nChoose your test\n");
	printf("1. Interactif test (src and dest separated)\n");
	printf("2. Test with overlap (src < dest)\n");
	printf("3. Test with overlap (dest < src)\n");
	scanf("%d", &choice);
	getchar();
	if (choice == 1)
	{
		printf("\nInstruction (1/3) : write a string (destination)\n");
		fgets(dest, sizeof(dest), stdin);
		dest[strcspn(dest, "\n")] = 0;
		strcpy(dest_copy, dest);
		strcpy(dest_original, dest);
		printf("\nInstruction (2/3) : write a string (source)\n");
		fgets(src, sizeof(src), stdin);
		src[strcspn(dest, "\n")] = 0;
		printf("\nInstruction (3/3) : write the numbers of octets\n");
		scanf("%zu", &n);
		getchar();
		printf("\n/!\\ Testing in progress /!\\\n\n");
		result = ft_memmove(dest, src, n);
		memmove(dest_copy, src, n);
	}
	else if (choice == 2 || choice == 3)
	{
		printf(RED "\n/!\\ Overlap Test (you don't need write anything) /!\\\n\n" RESET);
		strcpy(dest, "abcdefghij");
		strcpy(dest_copy, "abcdefghij");
		strcpy(dest_original, dest);
		n = 5;
		printf("Dest + Src (initial buffer) = \"%s\"\n", dest);
		if (choice == 2)
		{
			printf("\nAction = ft_memmove(dest + 2, dest, %zu)\n", n);
			result = ft_memmove(dest + 2, dest, n);
			memmove(dest_copy + 2, dest_copy, n);
			sleep (2);
		}
		else
		{
			printf("\nAction = ft_memmove(dest, dest + 2, %zu)\n", n);
			result = ft_memmove(dest, dest + 2, n);
			memmove(dest_copy, dest_copy + 2, n);
			sleep (2);
		}
	}
	else
	{
		printf(RED "Invalid number\n" RESET);
		return;
	}
	sleep((1));
	if (memcmp(dest, dest_copy, 100) == 0)
	{
		printf(GREEN "[SUCCESS]\n");
		printf("Original string	=	%s\n", dest_original);
		printf("New	string	=	%s\n", dest);
		printf(RESET);
	}
	else
	{
		if ((memcmp(dest, dest_copy, 100) != 0))
		{
			printf(RED "[Mismatch]\n");
			printf("ft_memmemove:	%s\n", dest);
			printf("memmove   :	%s\n", dest_copy);
		}
		if (result != dest)
		{
			printf(RED "[FAILED]\n");
			printf("Incorrect Pointer or NULL\n");
		}
		printf(RESET);
	}
	sleep(1);
	printf("\nTap 1 to make another test or 2 to return to main menu\n");
	choice = 0;
	scanf("%d", &choice);
	getchar();
	if (choice == 1)
	{
		test_ft_memmove();
	}
}

void test_ft_strlcpy()
{
	char	str[100];
	char	dest[100];
	char	dest_cpy[100];
	size_t	size;
	size_t	result;
	int		choice;

	memset(str, 0, 100);
	memset(dest, 0, 100);
	memset(dest_cpy, 0, 100);
	printf(UNDERLINE"\n=========="RESET"Testing "RED"ft_strlcpy" RESET UNDERLINE "==========\n" RESET);
	printf("Note: ft_strlcpy can't be compared to the original function. It's up to you to watch if it's working or not.\n\n");
	printf("\nInstruction (1/2) : write a string (source)\n");
	fgets(str, sizeof(str), stdin);
	str[strcspn(str, "\n")] = 0;
	printf("\nInstruction (2/2) : write the lenght\n");
	scanf("%zu", &size);
	getchar();
	printf("\n/!\\ Testing in progress /!\\\n\n");
	result = ft_strlcpy(dest, str, size);
	sleep(1);
	printf(YELLOW"Manual result\n");
	printf("New string (len = %zu) = %s\n", result, dest);
	printf(RESET);
	sleep(1);
	printf("\nTap 1 to make another test or 2 to return to main menu\n");
	choice = 0;
	scanf("%d", &choice);
	getchar();
	if (choice == 1)
	{
		test_ft_strlcpy();
	}
}

void test_ft_strlcat()
{
	char	str[100];
	char	dest[100];
	char	dest_original[100];
	char	dest_cpy[100];
	size_t	size;
	size_t	result;
	int		choice;

	memset(str, 0, 100);
	memset(dest, 0, 100);
	memset(dest_cpy, 0, 100);
	memset(dest_original, 0, 100);
	printf(UNDERLINE"\n=========="RESET"Testing "RED"ft_strlcat" RESET UNDERLINE "==========\n" RESET);
	printf("Note: ft_strlcat can't be compared to the original function. It's up to you to watch if it's working or not.\n\n");
	printf("\nInstruction (1/3) : write a string (destination)\n");
	fgets(dest, sizeof(dest), stdin);
	dest[strcspn(dest, "\n")] = 0;
	strcpy(dest_cpy, dest);
	strcpy(dest_original, dest);
	printf("\nInstruction (2/3) : write a string (source)\n");
	fgets(str, sizeof(str), stdin);
	str[strcspn(str, "\n")] = 0;
	printf("\nInstruction (3/3) : write the lenght\n");
	scanf("%zu", &size);
	getchar();
	printf("\n/!\\ Testing in progress /!\\\n\n");
	result = ft_strlcat(dest, str, size);
	sleep(1);
	printf(YELLOW"Manual result\n");
	printf("Original string : %s\n", dest_original);
	printf("New string (len = %zu) = %s\n", result, dest);
	printf(RESET);
	sleep(1);
	printf("\nTap 1 to make another test or 2 to return to main menu\n");
	choice = 0;
	scanf("%d", &choice);
	getchar();
	if (choice == 1)
	{
		test_ft_strlcat();
	}
}

void test_ft_toupper()
{
	char	c;
	char	result;
	int		choice;

	printf(UNDERLINE"\n=========="RESET"Testing "RED"ft_toupper" RESET UNDERLINE "==========\n" RESET);
	printf("\nInstruction (1/1) : write a printable character to perfom the test\n");
	scanf(" %c", &c);
	printf("\n/!\\ Testing in progress /!\\\n\n");
	result = ft_toupper(c);
	getchar();
	sleep(1);
	printf(PURPLE "%c is now %c \n", c, result);
	printf(RESET);
	sleep(1);
	printf("\nTap 1 to make another test or 2 to return to main menu\n");
	choice = 0;
	scanf("%d", &choice);
	getchar();
	if (choice == 1)
	{
		test_ft_toupper();
	}
}

void test_ft_tolower()
{
	char	c;
	char	result;
	int		choice;

	printf(UNDERLINE"\n=========="RESET"Testing "RED"ft_tolower" RESET UNDERLINE "==========\n" RESET);
	printf("\nInstruction (1/1) : write a printable character to perfom the test\n");
	scanf(" %c", &c);
	printf("\n/!\\ Testing in progress /!\\\n\n");
	result = ft_tolower(c);
	getchar();
	sleep(1);
	printf(PURPLE "%c is now %c \n", c, result);
	printf(RESET);
	sleep(1);
	printf("\nTap 1 to make another test or 2 to return to main menu\n");
	choice = 0;
	scanf("%d", &choice);
	getchar();
	if (choice == 1)
	{
		test_ft_tolower();
	}
}
void test_ft_strchr()
{
	char	str[100];
	char	c;
	char	*result;
	char	*result_cpy;
	int		choice;

	memset(str, 0, 100);
	printf(UNDERLINE"\n=========="RESET"Testing "RED"ft_strchr" RESET UNDERLINE "==========\n" RESET);
	printf("\nInstruction (1/2) : write a string\n");
	fgets(str, sizeof(str), stdin);
	str[strcspn(str, "\n")] = 0;
	printf("\nInstruction (2/2) : write a caracter (to find from the start)\n");
	scanf("%c", &c);
	getchar();
	printf("\n/!\\ Testing in progress /!\\\n\n");
	result = ft_strchr(str, c);
	result_cpy = strchr(str, c);
	sleep(1);
	if (result == result_cpy)
	{
		printf(GREEN "[SUCCESS]\n");
		if (result == NULL)
			printf("Can't find %c in %s\n", c, str);
		else
			printf("Character \"%c\" find : %s\n", c, result);
		printf(RESET);
	}
	else
	{
		printf(RED "[FAILED]\n");
		if (result == NULL)
			printf("ft_strchr : NULL\n");
		else
			printf("ft_strchr : %s\n", result);
		if (result_cpy == NULL)
			printf("strchr : NULL\n");
		else
			printf("strchr : %s\n", result_cpy);
		printf(RESET);
	}
	printf("\nTap 1 to make another test or 2 to return to main menu\n");
	choice = 0;
	scanf("%d", &choice);
	getchar();
	if (choice == 1)
	{
		test_ft_strchr();
	}
}

void test_ft_strrchr()
{
	char	str[100];
	char	c;
	char	*result;
	char	*result_cpy;
	int		choice;

	memset(str, 0, 100);
	printf(UNDERLINE"\n=========="RESET"Testing "RED"ft_strrchr" RESET UNDERLINE "==========\n" RESET);
	printf("\nInstruction (1/2) : write a string\n");
	fgets(str, sizeof(str), stdin);
	str[strcspn(str, "\n")] = 0;
	printf("\nInstruction (2/2) : write a caracter (to find from the start)\n");
	scanf("%c", &c);
	getchar();
	printf("\n/!\\ Testing in progress /!\\\n\n");
	result = ft_strrchr(str, c);
	result_cpy = strrchr(str, c);
	sleep(1);
	if (result == result_cpy)
	{
		printf(GREEN "[SUCCESS]\n");
		if (result == NULL)
			printf("Can't find %c in %s\n", c, str);
		else
			printf("Character \"%c\" find : %s\n", c, result);
		printf(RESET);
	}
	else
	{
		printf(RED "[FAILED]\n");
		if (result == NULL)
			printf("ft_strrchr : NULL\n");
		else
			printf("ft_strrchr : %s\n", result);
		if (result_cpy == NULL)
			printf("strrchr : NULL\n");
		else
			printf("strrchr : %s\n", result_cpy);
		printf(RESET);
	}
	printf("\nTap 1 to make another test or 2 to return to main menu\n");
	choice = 0;
	scanf("%d", &choice);
	getchar();
	if (choice == 1)
	{
		test_ft_strrchr();
	}
}

void test_ft_strncmp()
{
	char	str1[100];
	char	str2[100];
	size_t	size;
	int		result;
	int		result_original;
	int	choice;

	memset(str1, 0, 100);
	memset(str2, 0, 100);
	printf(UNDERLINE"\n=========="RESET"Testing "RED"ft_strncmp" RESET UNDERLINE "==========\n" RESET);
	printf("\nInstruction (1/3) : write the first string for comparison\n");
	fgets(str1, sizeof(str1), stdin);
	str1[strcspn(str1, "\n")] = 0;
	printf("\nInstruction (2/3) : write the second string for comparison\n");
	fgets(str2, sizeof(str1), stdin);
	str2[strcspn(str2, "\n")] = 0;
	printf("\nInstruction (3/3) : write the lenght\n");
	scanf("%zu", &size);
	getchar();
	printf("\n/!\\ Testing in progress /!\\\n\n");
	result = ft_strncmp(str1, str2, size);
	result_original = strncmp(str1, str2, size);
	sleep (1);
	if (result == result_original)
	{
		printf(GREEN "[SUCCESS]\n");
		printf("Return value = %d\n", result);
		printf(RESET);
	}
	else
	{
		printf(RED "[FAILED]\n");
		printf("ft_strncmp = %d\n", result);
		printf("strncmp = %d\n", result_original);
		printf(RESET);
	}
	printf("\nTap 1 to make another test or 2 to return to main menu\n");
	choice = 0;
	scanf("%d", &choice);
	getchar();
	if (choice == 1)
	{
		test_ft_strncmp();
	}
}

void test_ft_memchr()
{
	char	str[100];
	int		c;
	size_t	size;
	char	*result;
	char	*result_original;
	int		choice;

	memset(str, 0, 100);
	printf(UNDERLINE"\n=========="RESET"Testing "RED"ft_memchr" RESET UNDERLINE "==========\n" RESET);
	printf("\nInstruction (1/3) : write a string (memory zone)\n");
	fgets(str, sizeof(str), stdin);
	str[strcspn(str, "\n")] = 0;
	printf("\nInstruction (2/3) : write a character\n");
	scanf("%lc", &c);
	getchar();
	printf("\nInstruction (3/3) : write the numbers of octets\n");
	scanf("%zu", &size);
	getchar();
	printf("\n/!\\ Testing in progress /!\\\n\n");
	result = ft_memchr(str, c, size);
	result_original = memchr(str, c, size);
	sleep (1);
	if (result == result_original)
	{
		printf(GREEN "[SUCCESS]\n");
		if (result == NULL)
			printf("Character \"%c\" have not been found\n", c);
		else
			printf("Character \"%c\" find : %s\n", c, result);
		printf(RESET);
	}
	else
	{
		printf(RED "[FAILED]\n");
		printf("ft_memchr: %p\n", (void*)result);
		printf("memchr: %p\n", (void*)result_original);
		printf(RESET);
	}
	printf("\nTap 1 to make another test or 2 to return to main menu\n");
	choice = 0;
	scanf("%d", &choice);
	getchar();
	if (choice == 1)
	{
		test_ft_memchr();
	}
}

void test_ft_memcmp()
{
	char	str1[100];
	char	str2[100];
	size_t	size;
	int		result;
	int		result_original;
	int		choice;

	memset(str1, 0, 100);
	memset(str2, 0, 100);
	printf(UNDERLINE"\n=========="RESET"Testing "RED"ft_memcmp" RESET UNDERLINE "==========\n" RESET);
	printf("\nInstruction (1/3) : write the first string\n");
	fgets(str1, sizeof(str1), stdin);
	str1[strcspn(str1, "\n")] = 0;
	printf("\nInstruction (2/3) : write the second string\n");
	fgets(str2, sizeof(str2), stdin);
	str2[strcspn(str2, "\n")] = 0;
	printf("\nInstruction (3/3) : write the numbers of octets\n");
	scanf("%zu", &size);
	getchar();
	printf("\n/!\\ Testing in progress /!\\\n\n");
	result = ft_memcmp(str1, str2, size);
	result_original = memcmp(str1, str2, size);
	sleep (1);
	if (((result < 0) && (result_original < 0)) || ((result > 0) && (result_original > 0)) || ((result == 0) && (result_original == 0)))
	{
		printf(GREEN "[SUCCESS]\n");
		printf("ft_memcmp: %d\n", result);
		printf("memcmp: %d\n", result_original);
		printf(RESET);
	}
	else
	{
		printf(RED "[FAILED]\n");
		printf("ft_memcmp: %d\n", result);
		printf("memcmp: %d\n", result_original);
		printf(RESET);
	}
	printf("\nTap 1 to make another test or 2 to return to main menu\n");
	choice = 0;
	scanf("%d", &choice);
	getchar();
	if (choice == 1)
	{
		test_ft_memcmp();
	}
}

void test_ft_strnstr()
{
	char	haystack[100];
	char	needle[100];
	size_t	size;
	char	*result;
	int	choice;

	memset(haystack, 0, 100);
	memset(needle, 0, 100);
	printf(UNDERLINE"\n=========="RESET"Testing "RED"ft_strnstr" RESET UNDERLINE "==========\n" RESET);
	printf("Note: ft_strnstr can't be compared to the original function. It's up to you to watch if it's working or not.\n\n");
	printf("\nInstruction (1/3) : write the full string\n");
	fgets(haystack, sizeof(haystack), stdin);
	haystack[strcspn(haystack, "\n")] = 0;
	printf("\nInstruction (2/3) : write the word you want to find\n");
	fgets(needle, sizeof(needle), stdin);
	needle[strcspn(needle, "\n")] = 0;
	printf("\nInstruction (3/3) : write the lenght\n");
	scanf("%zu", &size);
	getchar();
	printf("\n/!\\ Testing in progress /!\\\n\n");
	result = ft_strnstr(haystack, needle, size);
	sleep (1);
	printf(YELLOW"Manual result\n");
	if (result == NULL)
	{
		printf("NULL or ERROR\n");
		printf("The word \"%s\" have not been found\n", needle);
		printf(RESET);
	}
	else
	{
		printf("\"%s\" find!\n Full sentence is: %s\n", needle, result);
		printf(RESET);
	}
	printf("\nTap 1 to make another test or 2 to return to main menu\n");
	choice = 0;
	scanf("%d", &choice);
	getchar();
	if (choice == 1)
	{
		test_ft_strnstr();
	}
}

void test_ft_atoi()
{
	char	str[100];
	int		result;
	int		result_original;
	int		choice;

	memset(str, 0, 100);
	printf(UNDERLINE"\n=========="RESET"Testing "RED"ft_atoi" RESET UNDERLINE "==========\n" RESET);
	printf("\nInstruction (1/1) : write the number you want to convert in int\n");
	fgets(str, sizeof(str), stdin);
	str[strcspn(str, "\n")] = 0;
	printf("\n/!\\ Testing in progress /!\\\n\n");
	result = ft_atoi(str);
	result_original = atoi(str);
	sleep (1);
	if (result == result_original)
	{
		printf(GREEN "[SUCCESS]\n");
		printf("\"%s\" have been converted to an int: %d", str, result);
		printf(RESET);
	}
	else
	{
		printf(RED "[FAILED]\n");
		printf("ft_atoi: %d\n", result);
		printf("atoi: %d\n", result_original);
		printf(RESET);
	}
	printf("\nTap 1 to make another test or 2 to return to main menu\n");
	choice = 0;
	scanf("%d", &choice);
	getchar();
	if (choice == 1)
	{
		test_ft_atoi();
	}
}

void test_ft_calloc()
{
	size_t	count;
	size_t	size;
	void	*ptr;
	void	*ptr_original;
	int		choice;

	printf(UNDERLINE"\n=========="RESET"Testing "RED"ft_calloc" RESET UNDERLINE "==========\n" RESET);
	printf("\nInstruction (1/2) : write the number of elements\n");
	scanf("%zu", &count);
	getchar();
	printf("\nInstruction (2/2) : write the size\n");
	scanf("%zu", &size);
	getchar();
	printf("\n/!\\ Testing in progress /!\\\n\n");
	ptr = ft_calloc(count, size);
	ptr_original = calloc(count, size);
	sleep (1);
	if (ptr == NULL && ptr_original == NULL)
	{
		printf(GREEN "[SUCCESS]\n");
		printf("NULL return for both so zero size or overflow\n");
		printf(RESET);
	}
	else if (ptr == NULL || ptr_original == NULL)
	{
		printf(RED "[FAILED]\n");
		printf("One function returned NULL, the other not\n");
		printf("ft_calloc:	%p\n", ptr);
		printf("calloc:	%p\n", ptr_original);
		printf(RESET);
	}
	else
	{
		if (memcmp(ptr, ptr_original, count * size) == 0)
		{
			printf(GREEN "[SUCCESS]\n");
			printf("Memory was allocated and correctly zero-initilialized");
			printf(RESET);
		}
		else
		{
			printf(RED "[MISMATCH]\n");
			printf("Memory was allocated but not correctly zero-initilialized");
			printf("ft_calloc:	%p\n", ptr);
			printf("calloc:	%p\n", ptr_original);
			printf(RESET);
		}
	}
	if (!ptr)
		free(ptr);
	if (!ptr_original)
		free(ptr_original);
	printf("\nTap 1 to make another test or 2 to return to main menu\n");
	choice = 0;
	scanf("%d", &choice);
	getchar();
	if (choice == 1)
	{
		test_ft_calloc();
	}
}

void test_ft_strdup()
{
	char	str[100];
	char	*result_original;
	char	*result;
	int		choice;

	memset(str, 0, 100);
	printf(UNDERLINE"\n=========="RESET"Testing "RED"ft_strdup" RESET UNDERLINE "==========\n" RESET);
	printf("\nInstruction (1/1) : write the string to duplicate\n");
	fgets(str, sizeof(str), stdin);
	str[strcspn(str, "\n")] = 0;
	printf("\n/!\\ Testing in progress /!\\\n\n");
	result = ft_strdup(str);
	result_original = strdup(str);
	sleep (1);
	if (result == NULL && result_original == NULL)
	{
		printf(GREEN "[SUCCESS]\n");
		printf("Both functions returned NULL\n");
		printf(RESET);
	}
	else if (result != NULL && result_original != NULL)
	{
		if (strcmp(result, result_original) == 0)
		{
			printf(GREEN "[SUCCESS]\n");
			printf("\"%s\" have been duplicated\n", result);
			printf(RESET);
		}
		else
		{
			printf(RED "[MISMATCH]\n");
			printf("ft_strdup:	%p\n", result);
			printf("strdup:		%p\n", result_original);
			printf(RESET);
		}
	}
	else
	{
		printf(RED "[FAILED]\n");
		printf("ft_strdup:	%p\n", (void*)result);
		printf("strdup:		%p\n", (void*)result_original);
		printf(RESET);
	}
	if (result != NULL)
		free (result);
	if (result_original != NULL)
		free (result_original);
	printf("\nTap 1 to make another test or 2 to return to main menu\n");
	choice = 0;
	scanf("%d", &choice);
	getchar();
	if (choice == 1)
	{
		test_ft_strdup();
	}
}

void test_ft_substr()
{
	char	str[100];
	int		start;
	size_t	size;
	char	*result;
	int		choice;

	memset(str, 0, 100);
	printf(UNDERLINE"\n=========="RESET"Testing "RED"ft_substr" RESET UNDERLINE "==========\n" RESET);
	printf("Note: ft_substr can't be compared to the original function. It's up to you to watch if it's working or not.\n\n");
	printf("\nInstruction (1/3) : write the string you want\n");
	fgets(str, sizeof(str), stdin);
	str[strcspn(str, "\n")] = 0;
	printf("\nInstruction (2/3) : when do you want to start (number)\n");
	scanf("%d", &start);
	getchar();
	printf("\nInstruction (3/3) : write the size\n");
	scanf("%zu", &size);
	getchar();
	printf("\n/!\\ Testing in progress /!\\\n\n");
	result = ft_substr(str, start, size);
	sleep (1);
	printf(YELLOW"Manual result\n");
	if (result == NULL)
	{
		printf("Function returned NULL\n");
		printf(RESET);
	}
	else
	{
		printf("Source:	%s\n", str);
		printf("Result:	%s\n", result);
		printf(RESET);
	}
	if (result != NULL)
		free (result);
	printf("\nTap 1 to make another test or 2 to return to main menu\n");
	choice = 0;
	scanf("%d", &choice);
	getchar();
	if (choice == 1)
	{
		test_ft_substr();
	}
}

void test_ft_strjoin()
{
	char	str1[100];
	char	str2[100];
	char	*result;
	int		choice;

	memset(str1, 0, 100);
	memset(str2, 0, 100);
	printf(UNDERLINE"\n=========="RESET"Testing "RED"ft_strjoin" RESET UNDERLINE "==========\n" RESET);
	printf("Note: ft_strjoin can't be compared to the original function. It's up to you to watch if it's working or not.\n\n");
	printf("\nInstruction (1/2) : write the first string\n");
	fgets(str1, sizeof(str1), stdin);
	str1[strcspn(str1, "\n")] = 0;
	printf("\nInstruction (2/2) : write the second strin\n");
	fgets(str2, sizeof(str2), stdin);
	str2[strcspn(str2, "\n")] = 0;
	printf("\n/!\\ Testing in progress /!\\\n\n");
	result = ft_strjoin(str1, str2);
	sleep (1);
	printf(YELLOW"Manual result\n");
	if (result == NULL)
	{
		printf("Function returned NULL\n");
		printf(RESET);
	}
	else
	{
		printf("Result:	%s\n", result);
		printf(RESET);
	}
	if (result != NULL)
		free(result);
	printf("\nTap 1 to make another test or 2 to return to main menu\n");
	choice = 0;
	scanf("%d", &choice);
	getchar();
	if (choice == 1)
	{
		test_ft_strjoin();
	}
}

void test_ft_strtrim()
{
	char	str[100];
	char	set[100];
	char	*result;
	int		choice;

	memset(str, 0, 100);
	memset(set, 0, 100);
	printf(UNDERLINE"\n=========="RESET"Testing "RED"ft_strtrim" RESET UNDERLINE "==========\n" RESET);
	printf("Note: ft_strtrim can't be compared to the original function. It's up to you to watch if it's working or not.\n\n");
	printf("\nInstruction (1/2) : write the first string\n");
	fgets(str, sizeof(str), stdin);
	str[strcspn(str, "\n")] = 0;
	printf("\nInstruction (2/2) : write the characters (or words) to trim\n");
	fgets(set, sizeof(set), stdin);
	set[strcspn(set, "\n")] = 0;
	printf("\n/!\\ Testing in progress /!\\\n\n");
	result = ft_strtrim(str, set);
	sleep (1);
	printf(YELLOW"Manual result\n");
	if (result == NULL)
	{
		printf("Function returned NULL\n");
		printf(RESET);
	}
	else
	{
		printf("Result:	%s\n", result);
		printf(RESET);
	}
	if (result != NULL)
		free(result);
	printf("\nTap 1 to make another test or 2 to return to main menu\n");
	choice = 0;
	scanf("%d", &choice);
	getchar();
	if (choice == 1)
	{
		test_ft_strtrim();
	}
}

void test_ft_split()
{
	char	str[100];
	char	c;
	char	**result;
	int		i;
	int		choice;

	memset(str, 0, 100);
	printf(UNDERLINE"\n=========="RESET"Testing "RED"ft_split" RESET UNDERLINE "==========\n" RESET);
	printf("Note: ft_split can't be compared to the original function. It's up to you to watch if it's working or not.\n\n");
	printf("\nInstruction (1/2) : write the string you want\n");
	fgets(str, sizeof(str), stdin);
	str[strcspn(str, "\n")] = 0;
	printf("\nInstruction (2/2) : write the delimiter character\n");
	scanf("%c", &c);
	getchar();
	printf("\n/!\\ Testing in progress /!\\\n\n");
	result = ft_split(str, c);
	sleep (1);
	printf(YELLOW"Manual result\n");
	if (result == NULL)
	{
		printf("Function returned NULL\n");
		printf(RESET);
	}
	else
	{
		i = 0;
		while (result[i] != NULL)
		{
			printf("[%s] ", result[i]);
			i++;
		}
		printf("[NULL]\n");
		printf(RESET);
	}
	if (result != NULL)
	{
		i = 0;
		while (result[i] != NULL)
		{
			free (result[i]);
			i++;
		}
		free (result);
	}
	printf("\nTap 1 to make another test or 2 to return to main menu\n");
	choice = 0;
	scanf("%d", &choice);
	getchar();
	if (choice == 1)
	{
		test_ft_split();
	}
}

void test_ft_itoa()
{
	int		number;
	char	*result;
	int		choice;

	printf(UNDERLINE"\n=========="RESET"Testing "RED"ft_itoa" RESET UNDERLINE "==========\n" RESET);
	printf("Note: ft_itoa can't be compared to the original function. It's up to you to watch if it's working or not.\n\n");
	printf("\nInstruction (1/1) : write number to convert in char\n");
	scanf("%d", &number);
	getchar();
	printf("\n/!\\ Testing in progress /!\\\n\n");
	result = ft_itoa(number);
	sleep (1);
	printf(YELLOW"Manual result\n");
	if (result == NULL)
	{
		printf("Function returned NULL\n");
		printf(RESET);
	}
	else
	{
		printf("Result:	%s\n", result);
		printf(RESET);
	}
	if (result != NULL)
		free(result);
	printf("\nTap 1 to make another test or 2 to return to main menu\n");
	choice = 0;
	scanf("%d", &choice);
	getchar();
	if (choice == 1)
	{
		test_ft_itoa();
	}
}

void test_ft_strmapi()
{
	char	str[100];
	char	*result;
	int		choice;

	memset(str, 0, 100);
	printf(UNDERLINE"\n=========="RESET"Testing "RED"ft_strmapi" RESET UNDERLINE "==========\n" RESET);
	printf("Note: ft_strmapi can't be compared to the original function. It's up to you to watch if it's working or not.\n");
	printf("You can modify the function in the main.c, at the top of the file.\n");
	printf("The actuel function replaces uppercase characters with their lowercase equivalents and vice versa\n\n");
	printf("\nInstruction (1/1) : write the string you want\n");
	fgets(str, sizeof(str), stdin);
	str[strcspn(str, "\n")] = 0;
	printf("\n/!\\ Testing in progress /!\\\n\n");
	result = ft_strmapi(str, ft_map_strmapi);
	sleep (1);
	printf(YELLOW"Manual result\n");
	if (result == NULL)
	{
		printf("Function returned NULL\n");
		printf(RESET);
	}
	else
	{
		printf("Result:	%s\n", result);
		printf(RESET);
	}
	if (result != NULL)
		free(result);
	printf("\nTap 1 to make another test or 2 to return to main menu\n");
	choice = 0;
	scanf("%d", &choice);
	getchar();
	if (choice == 1)
	{
		test_ft_strmapi();
	}
}

void test_ft_striteri()
{
	char	str[100];
	int		choice;

	memset(str, 0, 100);
	printf(UNDERLINE"\n=========="RESET"Testing "RED"ft_striteri" RESET UNDERLINE "==========\n" RESET);
	printf("Note: ft_striteri can't be compared to the original function. It's up to you to watch if it's working or not.\n");
	printf("You can modify the function in the main.c, at the top of the file.\n");
	printf("The actual function replaces every characters by the next one (a->b / j->k / 5->6)\n\n");
	printf("\nInstruction (1/1) : write the string you want to modify\n");
	fgets(str, sizeof(str), stdin);
	str[strcspn(str, "\n")] = 0;
	printf("\n/!\\ Testing in progress /!\\\n\n");
	ft_striteri(str, ft_map_striteri);
	sleep (1);
	printf(YELLOW"Manual result\n");
	printf("Result:	%s\n", str);
	printf(RESET);
	printf("\nTap 1 to make another test or 2 to return to main menu\n");
	choice = 0;
	scanf("%d", &choice);
	getchar();
	if (choice == 1)
	{
		test_ft_striteri();
	}
}

void test_ft_putchar_fd()
{
	char	c;
	int		fd;
	int		choice;

	printf(UNDERLINE"\n=========="RESET"Testing "RED"ft_putchar_fd" RESET UNDERLINE "==========\n" RESET);
	printf("Note: ft_putchar_fd can't be compared to the original function. It's up to you to watch if it's working or not.\n\n");
	printf("\nInstruction (1/2) : write a caracter\n");
	scanf("%c", &c);
	getchar();
	printf("\nInstruction (2/2) : choose the fd\n");
	scanf("%d", &fd);
	printf("\n/!\\ Testing in progress /!\\\n\n");
	sleep (1);
	printf(YELLOW"Manual result\n");
	printf("Check is you see the caracter :\n");
	printf("" RESET);
	ft_putchar_fd(c, fd);
	printf(RESET);
	printf("\nTap 1 to make another test or 2 to return to main menu\n");
	choice = 0;
	scanf("%d", &choice);
	getchar();
	if (choice == 1)
	{
		test_ft_putchar_fd();
	}
}

void test_ft_putstr_fd()
{
	char	str[100];
	int		fd;
	int		choice;

	memset(str, 0, 100);
	printf(UNDERLINE"\n=========="RESET"Testing "RED"ft_putstr_fd" RESET UNDERLINE "==========\n" RESET);
	printf("Note: ft_putstr_fd can't be compared to the original function. It's up to you to watch if it's working or not.\n\n");
	printf("\nInstruction (1/2) : write a string\n");
	fgets(str, sizeof(str), stdin);
	str[strcspn(str, "\n")] = 0;
	printf("\nInstruction (2/2) : choose the fd\n");
	scanf("%d", &fd);
	printf("\n/!\\ Testing in progress /!\\\n\n");
	sleep (1);
	printf(YELLOW"Manual result\n");
	printf("Check is you see the string :\n");
	printf("" RESET);
	ft_putstr_fd(str, fd);
	printf(RESET);
	printf("\nTap 1 to make another test or 2 to return to main menu\n");
	choice = 0;
	scanf("%d", &choice);
	getchar();
	if (choice == 1)
	{
		test_ft_putstr_fd();
	}
}
void test_ft_putendl_fd()
{
	char	str[100];
	int		fd;
	int		choice;

	memset(str, 0, 100);
	printf(UNDERLINE"\n=========="RESET"Testing "RED"ft_putendl_fd" RESET UNDERLINE "==========\n" RESET);
	printf("Note: ft_putendl_fd can't be compared to the original function. It's up to you to watch if it's working or not.\n\n");
	printf("\nInstruction (1/2) : write a string\n");
	fgets(str, sizeof(str), stdin);
	str[strcspn(str, "\n")] = 0;
	printf("\nInstruction (2/2) : choose the fd\n");
	scanf("%d", &fd);
	printf("\n/!\\ Testing in progress /!\\\n\n");
	sleep (1);
	printf(YELLOW"Manual result\n");
	printf("Check is you see the string and a newline :\n"RESET);
	printf(RESET);
	ft_putendl_fd(str, fd);
	printf(RESET);
	sleep (2);
	printf("\nTap 1 to make another test or 2 to return to main menu\n");
	choice = 0;
	scanf("%d", &choice);
	getchar();
	if (choice == 1)
	{
		test_ft_putendl_fd();
	}
}

void test_ft_putnbr_fd()
{
	int	n;
	int	fd;
	int	choice;

	printf(UNDERLINE"\n=========="RESET"Testing "RED"ft_putnbr_fd" RESET UNDERLINE "==========\n" RESET);
	printf("Note: ft_putnbr_fd can't be compared to the original function. It's up to you to watch if it's working or not.\n\n");
	printf("\nInstruction (1/2) : write a number\n");
	scanf("%d", &n);
	printf("\nInstruction (2/2) : choose the fd\n");
	scanf("%d", &fd);
	printf("\n/!\\ Testing in progress /!\\\n\n");
	sleep (1);
	printf(YELLOW"Manual result\n");
	printf("Check is you see the number :\n");
	printf("" RESET);
	ft_putnbr_fd(n, fd);
	sleep (2);
	printf("\nTap 1 to make another test or 2 to return to main menu\n");
	choice = 0;
	scanf("%d", &choice);
	getchar();
	if (choice == 1)
	{
		test_ft_putnbr_fd();
	}
}
void test_ft_lstnew()
{
	t_list	*list = NULL;
	t_list *elem1;
	char	str[100];
	int	choice;

	memset(str, 0, 100);
	printf(UNDERLINE"\n=========="RESET"Testing "RED"ft_lstnew" RESET UNDERLINE "==========\n" RESET);
	printf("Note: ft_lst can't be compared to an original function. It's up to you to watch if it's working or not.\n\n");
	printf("\nInstruction (1/1) : write a string to store in the new node\n");
	fgets(str, sizeof(str), stdin);
	str[strcspn(str, "\n")] = 0;
	elem1 = ft_lstnew(ft_strdup(str));
	ft_lstadd_front(&list, elem1);
	printf("\n/!\\ Testing in progress /!\\\n\n");
	sleep (1);
	printf(YELLOW"Manual result\n");
	printf("List of your element\n\n");
	printf(RESET);
	print_list(list);
	ft_lstclear(&list, ft_del);
	sleep (2);
	printf("\nTap 1 to make another test or 2 to return to main menu\n");
	choice = 0;
	scanf("%d", &choice);
	getchar();
	if (choice == 1)
	{
		test_ft_lstnew();
	}
}
void test_ft_lstadd_front()
{
	t_list	*list = NULL;
	t_list *elem1 = ft_lstnew(ft_strdup("Sun"));
	t_list *elem2 = ft_lstnew(ft_strdup("Home"));
	t_list *elem3 = ft_lstnew(ft_strdup("Music"));
	t_list *elem4;
	char	str[100];
	int	choice;

	memset(str, 0, 100);
	printf(UNDERLINE"\n=========="RESET"Testing "RED"ft_lstadd_front" RESET UNDERLINE "==========\n" RESET);
	printf("Note: ft_lstadd_front can't be compared to an original function. It's up to you to watch if it's working or not.\n\n");
	sleep(1);
	ft_lstadd_back(&list, elem1);
	ft_lstadd_back(&list, elem2);
	ft_lstadd_back(&list, elem3);
	printf("\nHere is the list\n\n");
	print_list(list);
	sleep (2);
	printf("\n\nInstruction (1/1) : write a string to store in the new node. It will be the first in the list.\n");
	fgets(str, sizeof(str), stdin);
	str[strcspn(str, "\n")] = 0;
	elem4 = ft_lstnew(ft_strdup(str));
	ft_lstadd_front(&list, elem4);
	printf("\n/!\\ Testing in progress /!\\\n\n");
	sleep (1);
	printf(YELLOW"Manual result\n");
	printf("List of your element\n\n");
	printf(RESET);
	print_list(list);
	ft_lstclear(&list, ft_del);
	sleep (2);
	printf("\nTap 1 to make another test or 2 to return to main menu\n");
	choice = 0;
	scanf("%d", &choice);
	getchar();
	if (choice == 1)
	{
		test_ft_lstadd_front();
	}
}
void test_ft_lstsize()
{
	t_list	*list = NULL;
	t_list *elem1 = ft_lstnew(ft_strdup("Sun"));
	t_list *elem2 = ft_lstnew(ft_strdup("Home"));
	t_list *elem3 = ft_lstnew(ft_strdup("Music"));
	t_list *elem4;
	int		size;
	char	str[100];
	int	choice;

	size = 0;
	memset(str, 0, 100);
	printf(UNDERLINE"\n=========="RESET"Testing "RED"ft_lstadd_front" RESET UNDERLINE "==========\n" RESET);
	printf("Note: ft_lstadd_front can't be compared to an original function. It's up to you to watch if it's working or not.\n\n");
	sleep(1);
	ft_lstadd_back(&list, elem1);
	ft_lstadd_back(&list, elem2);
	ft_lstadd_back(&list, elem3);
	printf("\nHere is the list\n\n");
	print_list(list);
	sleep (2);
	printf("\n\nInstruction (1/1) : write a string to store in the new node\n");
	fgets(str, sizeof(str), stdin);
	str[strcspn(str, "\n")] = 0;
	elem4 = ft_lstnew(ft_strdup(str));
	ft_lstadd_front(&list, elem4);
	size = ft_lstsize(list);
	printf("\n/!\\ Testing in progress /!\\\n\n");
	sleep (1);
	printf(YELLOW"Manual result\n");
	printf("List of your element\n\n");
	printf(RESET);
	print_list(list);
	printf("\n");
	printf("Size = %d\n", size);
	ft_lstclear(&list, ft_del);
	sleep (2);
	printf("\nTap 1 to make another test or 2 to return to main menu\n");
	choice = 0;
	scanf("%d", &choice);
	getchar();
	if (choice == 1)
	{
		test_ft_lstadd_front();
	}
}
void test_ft_lstlast()
{
	t_list	*list = NULL;
	t_list *elem1 = ft_lstnew(ft_strdup("Sun"));
	t_list *elem2 = ft_lstnew(ft_strdup("Home"));
	t_list *elem3 = ft_lstnew(ft_strdup("Music"));
	t_list *elem4;
	t_list	*last_element;
	char	str[100];
	int	choice;

	memset(str, 0, 100);
	printf(UNDERLINE"\n=========="RESET"Testing "RED"ft_lstlast" RESET UNDERLINE "==========\n" RESET);
	printf("Note: ft_lstlast can't be compared to an original function. It's up to you to watch if it's working or not.\n\n");
	sleep(1);
	ft_lstadd_back(&list, elem1);
	ft_lstadd_back(&list, elem2);
	ft_lstadd_back(&list, elem3);
	printf("\nHere is the list\n\n");
	print_list(list);
	sleep (2);
	printf("\n\nInstruction (1/1) : write a string to store in the new node\n");
	fgets(str, sizeof(str), stdin);
	str[strcspn(str, "\n")] = 0;
	elem4 = ft_lstnew(ft_strdup(str));
	ft_lstadd_back(&list, elem4);
	last_element = ft_lstlast(list);
	printf("\n/!\\ Testing in progress /!\\\n\n");
	sleep (1);
	printf(YELLOW"Manual result\n");
	printf("List of your element\n\n");
	printf(RESET);
	print_list(list);
	printf("\n");
	if (last_element != NULL)
		printf("Last element is = %s\n", (char *)last_element->content);
	else
		printf("Last element was empty or NULL, or ERROR\n");
	ft_lstclear(&list, ft_del);
	sleep (2);
	printf("\nTap 1 to make another test or 2 to return to main menu\n");
	choice = 0;
	scanf("%d", &choice);
	getchar();
	if (choice == 1)
	{
		test_ft_lstlast();
	}
}
void test_ft_lstadd_back()
{
	t_list	*list = NULL;
	t_list *elem1 = ft_lstnew(ft_strdup("Sun"));
	t_list *elem2 = ft_lstnew(ft_strdup("Home"));
	t_list *elem3 = ft_lstnew(ft_strdup("Music"));
	t_list *elem4;
	char	str[100];
	int	choice;

	memset(str, 0, 100);
	printf(UNDERLINE"\n=========="RESET"Testing "RED"ft_lstadd_back" RESET UNDERLINE "==========\n" RESET);
	printf("Note: ft_lstadd_back can't be compared to an original function. It's up to you to watch if it's working or not.\n\n");
	sleep(1);
	ft_lstadd_back(&list, elem1);
	ft_lstadd_back(&list, elem2);
	ft_lstadd_back(&list, elem3);
	printf("\nHere is the list\n\n");
	print_list(list);
	sleep (2);
	printf("\n\nInstruction (1/1) : write a string to store in the new node. It will be the last in the list.\n");
	fgets(str, sizeof(str), stdin);
	str[strcspn(str, "\n")] = 0;
	elem4 = ft_lstnew(ft_strdup(str));
	ft_lstadd_back(&list, elem4);
	printf("\n/!\\ Testing in progress /!\\\n\n");
	sleep (1);
	printf(YELLOW"Manual result\n");
	printf("List of your element\n\n");
	printf(RESET);
	print_list(list);
	ft_lstclear(&list, ft_del);
	sleep (2);sleep (2);
	printf("\nTap 1 to make another test or 2 to return to main menu\n");
	choice = 0;
	scanf("%d", &choice);
	getchar();
	if (choice == 1)
	{
		test_ft_lstadd_back();
	}
}
void test_ft_lstdelone()
{
	t_list	*list = NULL;
	t_list	*elem1 = ft_lstnew(ft_strdup("Sun"));
	t_list	*elem2 = ft_lstnew(ft_strdup("Home"));
	t_list	*elem3 = ft_lstnew(ft_strdup("Music"));
	t_list	*elem4 = ft_lstnew(ft_strdup("Ninja"));
	t_list	*elem5 = ft_lstnew(ft_strdup("Silksong"));
	t_list	*elem6 = ft_lstnew(ft_strdup("Clair"));
	t_list	*elem7 = ft_lstnew(ft_strdup("Code"));
	t_list	*elem8;
	t_list	*temp;
	char	str[100];
	int		choice;

	memset(str, 0, 100);
	printf(UNDERLINE"\n=========="RESET"Testing "RED"ft_lstdelone" RESET UNDERLINE "==========\n" RESET);
	printf("Note: ft_lstdelone can't be compared to an original function. It's up to you to watch if it's working or not.\n\n");
	sleep(1);
	ft_lstadd_back(&list, elem1);
	ft_lstadd_back(&list, elem2);
	ft_lstadd_back(&list, elem3);
	ft_lstadd_back(&list, elem4);
	ft_lstadd_back(&list, elem5);
	ft_lstadd_back(&list, elem6);
	ft_lstadd_back(&list, elem7);
	printf("\nHere is the list\n\n");
	print_list(list);
	sleep (2);
	printf("\n\nInstruction (1/1) : write a string to store in the new node. It will be the last in the list.\n");
	fgets(str, sizeof(str), stdin);
	str[strcspn(str, "\n")] = 0;
	elem8 = ft_lstnew(ft_strdup(str));
	ft_lstadd_back(&list, elem8);
	sleep (2);
	printf("Deleting node \"Music\"\n...");
	temp = elem2;
	temp->next = elem3->next;
	ft_lstdelone(elem3, ft_del);
	sleep (2);
	printf("\n/!\\ Testing in progress /!\\\n\n");
	sleep (1);
	printf(YELLOW"Manual result\n");
	printf("List of your element\n\n");
	printf(RESET);
	print_list(list);
	ft_lstclear(&list, ft_del);
	sleep (2);
	printf("\nTap 1 to make another test or 2 to return to main menu\n");
	choice = 0;
	scanf("%d", &choice);
	getchar();
	if (choice == 1)
	{
		test_ft_lstdelone();
	}
}
void test_ft_lstclear()
{
	t_list	*list = NULL;
	t_list	*elem1 = ft_lstnew(ft_strdup("Sun"));
	t_list	*elem2 = ft_lstnew(ft_strdup("Home"));
	t_list	*elem3 = ft_lstnew(ft_strdup("Music"));
	t_list	*elem4 = ft_lstnew(ft_strdup("Ninja"));
	t_list	*elem5 = ft_lstnew(ft_strdup("Silksong"));
	t_list	*elem6 = ft_lstnew(ft_strdup("Clair"));
	t_list	*elem7 = ft_lstnew(ft_strdup("Code"));
	t_list	*elem8;
	char	str[100];
	int		choice;

	memset(str, 0, 100);
	printf(UNDERLINE"\n=========="RESET"Testing "RED"ft_lstclear" RESET UNDERLINE "==========\n" RESET);
	printf("Note: ft_lstclear can't be compared to an original function. It's up to you to watch if it's working or not.\n\n");
	sleep(1);
	ft_lstadd_back(&list, elem1);
	ft_lstadd_back(&list, elem2);
	ft_lstadd_back(&list, elem3);
	ft_lstadd_back(&list, elem4);
	ft_lstadd_back(&list, elem5);
	ft_lstadd_back(&list, elem6);
	ft_lstadd_back(&list, elem7);
	printf("\nHere is the list\n\n");
	print_list(list);
	sleep (2);
	printf("\n\nInstruction (1/1) : write a string to store in the new node. It will be the last in the list.\n");
	fgets(str, sizeof(str), stdin);
	str[strcspn(str, "\n")] = 0;
	elem8 = ft_lstnew(ft_strdup(str));
	ft_lstadd_back(&list, elem8);
	sleep (2);
	printf("Deleting node \"Music\"\n...");
	ft_lstclear(&list, ft_del);
	sleep (2);
	printf("\n/!\\ Testing in progress /!\\\n\n");
	sleep (1);
	printf(YELLOW"Manual result\n");
	printf("List of your element\n\n");
	printf(RESET);
	print_list(list);
	if (list == NULL)
		printf(GREEN "\n[SUCCESS] The list pointer is now NULL.\n" RESET);
	else
		printf(RED "\n[FAILED] The list pointer is NOT NULL.\n" RESET);
	sleep (2);
	printf("\nTap 1 to make another test or 2 to return to main menu\n");
	choice = 0;
	scanf("%d", &choice);
	getchar();
	if (choice == 1)
	{
		test_ft_lstclear();
	}
}
void test_ft_lstiter()
{
	t_list	*list = NULL;
	t_list	*elem1 = ft_lstnew(ft_strdup("Sun"));
	t_list	*elem2 = ft_lstnew(ft_strdup("Home"));
	t_list	*elem3 = ft_lstnew(ft_strdup("Music"));
	t_list	*elem4 = ft_lstnew(ft_strdup("Ninja"));
	t_list	*elem5 = ft_lstnew(ft_strdup("Silksong"));
	t_list	*elem6 = ft_lstnew(ft_strdup("Clair"));
	t_list	*elem7 = ft_lstnew(ft_strdup("Code"));
	t_list	*elem8;
	char	str[100];
	int		choice;

	memset(str, 0, 100);
	printf(UNDERLINE"\n=========="RESET"Testing "RED"ft_lstiter" RESET UNDERLINE "==========\n" RESET);
	printf("Note: ft_lstiter can't be compared to an original function. It's up to you to watch if it's working or not.\n\n");
	printf("You can modify the function in the main.c, at the top of the file.\n");
	printf("The actuel function replaces the following letters : 'o'->0 / 'a'->4 / 'x'->3\n\n");
	sleep(2);
	ft_lstadd_back(&list, elem1);
	ft_lstadd_back(&list, elem2);
	ft_lstadd_back(&list, elem3);
	ft_lstadd_back(&list, elem4);
	ft_lstadd_back(&list, elem5);
	ft_lstadd_back(&list, elem6);
	ft_lstadd_back(&list, elem7);
	printf("\nHere is the list\n\n");
	print_list(list);
	sleep (2);
	printf("\n\nInstruction (1/1) : write a string to store in the new node. It will be the last in the list.\n");
	fgets(str, sizeof(str), stdin);
	str[strcspn(str, "\n")] = 0;
	elem8 = ft_lstnew(ft_strdup(str));
	ft_lstadd_back(&list, elem8);
	ft_lstiter(list, ft_map_lstiter);
	sleep (2);
	printf("Applying function \n...");
	sleep (2);
	printf("\n/!\\ Testing in progress /!\\\n\n");
	sleep (1);
	printf(YELLOW"Manual result\n");
	printf("List of your element\n\n");
	printf(RESET);
	print_list(list);
	ft_lstclear(&list, ft_del);
	sleep (2);
	printf("\nTap 1 to make another test or 2 to return to main menu\n");
	choice = 0;
	scanf("%d", &choice);
	getchar();
	if (choice == 1)
	{
		test_ft_lstiter();
	}
}
void test_ft_lstmap()
{
	t_list	*list = NULL;
	t_list	*new_list = NULL;
	t_list	*elem1 = ft_lstnew(ft_strdup("Sun"));
	t_list	*elem2 = ft_lstnew(ft_strdup("Home"));
	t_list	*elem3 = ft_lstnew(ft_strdup("Music"));
	t_list	*elem4 = ft_lstnew(ft_strdup("Ninja"));
	t_list	*elem5 = ft_lstnew(ft_strdup("Silksong"));
	t_list	*elem6 = ft_lstnew(ft_strdup("Clair"));
	t_list	*elem7 = ft_lstnew(ft_strdup("Code"));
	t_list	*elem8;
	char	str[100];
	int		choice;

	memset(str, 0, 100);
	printf(UNDERLINE"\n=========="RESET"Testing "RED"ft_lsmap" RESET UNDERLINE "==========\n" RESET);
	printf("Note: ft_lsmap can't be compared to an original function. It's up to you to watch if it's working or not.\n\n");
	printf("You can modify the function in the main.c, at the top of the file.\n");
	printf("The actuel function replaces the even letters by 0 and odd by 1\n\n");
	sleep(2);
	ft_lstadd_back(&list, elem1);
	ft_lstadd_back(&list, elem2);
	ft_lstadd_back(&list, elem3);
	ft_lstadd_back(&list, elem4);
	ft_lstadd_back(&list, elem5);
	ft_lstadd_back(&list, elem6);
	ft_lstadd_back(&list, elem7);
	printf("\nHere is the original list\n\n");
	print_list(list);
	sleep (2);
	printf("\n\nInstruction (1/1) : write a string to store in the new node. It will be the last in the list.\n");
	fgets(str, sizeof(str), stdin);
	str[strcspn(str, "\n")] = 0;
	elem8 = ft_lstnew(ft_strdup(str));
	ft_lstadd_back(&list, elem8);
	new_list = ft_lstmap(list, ft_map_lstmap, ft_del);
	sleep (2);
	printf("Applying function \n...");
	sleep (2);
	printf("\n/!\\ Testing in progress /!\\\n\n");
	sleep (1);
	printf(YELLOW"Manual result\n");
	printf("New list of your element\n\n");
	printf(RESET);
	print_list(new_list);
	ft_lstclear(&list, ft_del);
	ft_lstclear(&new_list, ft_del);
	sleep (2);
	printf("\nTap 1 to make another test or 2 to return to main menu\n");
	choice = 0;
	scanf("%d", &choice);
	getchar();
	if (choice == 1)
	{
		test_ft_lstmap();
	}
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
		else if (choice == 10)
			test_ft_memmove();
		else if (choice == 11)
			test_ft_strlcpy();
		else if (choice == 12)
			test_ft_strlcat();
		else if (choice == 13)
			test_ft_toupper();
		else if (choice == 14)
			test_ft_tolower();
		else if (choice == 15)
			test_ft_strchr();
		else if (choice == 16)
			test_ft_strrchr();
		else if (choice == 17)
			test_ft_strncmp();
		else if (choice == 18)
			test_ft_memchr();
		else if (choice == 19)
			test_ft_memcmp();
		else if (choice == 20)
			test_ft_strnstr();
		else if (choice == 21)
			test_ft_atoi();
		else if (choice == 22)
			test_ft_calloc();
		else if (choice == 23)
			test_ft_strdup();
		else if (choice == 24)
			test_ft_substr();
		else if (choice == 25)
			test_ft_strjoin();
		else if (choice == 26)
			test_ft_strtrim();
		else if (choice == 27)
			test_ft_split();
		else if (choice == 28)
			test_ft_itoa();
		else if (choice == 29)
			test_ft_strmapi();
		else if (choice == 30)
			test_ft_striteri();
		else if (choice == 31)
			test_ft_putchar_fd();
		else if (choice == 32)
			test_ft_putstr_fd();
		else if (choice == 33)
			test_ft_putendl_fd();
		else if (choice == 34)
			test_ft_putnbr_fd();
		else if (choice == 35)
			test_ft_lstnew();
		else if (choice == 36)
			test_ft_lstadd_front();
		else if (choice == 37)
			test_ft_lstsize();
		else if (choice == 38)
			test_ft_lstlast();
		else if (choice == 39)
			test_ft_lstadd_back();
		else if (choice == 40)
			test_ft_lstdelone();
		else if (choice == 41)
			test_ft_lstclear();
		else if (choice == 42)
			test_ft_lstiter();
		else if (choice == 43)
			test_ft_lstmap();
		else if (choice == 0)
			printf("Goodbye!\n");
		else
			printf(RED "Invalid number. Please, put a number that exist in the list.");
		if (choice != 0 && choice >= 1 && choice <= 43)
		{
			printf("\n(Press Enter to return to the menu)");
			getchar();
		}
	}
	return (0);
}
