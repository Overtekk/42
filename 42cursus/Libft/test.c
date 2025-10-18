#include <stdio.h>
#include <assert.h>
#include <string.h>
#include <stdlib.h>
#include <ctype.h>
#include "libft.h"
#include "ft_strlen.c"

int	char_count(char const *s1, char const *set)
{
	int	count;
	int	i;

	count = 0;
	i = 0;
	while (s1[i])
	{
		if (s1[i] == set[0])
			count++;
		i++;
	}
	return (count);

}

char	*ft_strtrim(char const *s1, char const *set)
{
	char	*dup;
	int		len;
	int		i;

	len = ft_strlen(s1) - char_count(s1, set);
	i = 0;
	dup = malloc(len + 1);
	if (!dup)
		return (NULL);
	while (s1[i] != 0)
	{
		if (s1[i] == set[0])
				s1++;
		dup[i] = s1[i];
		i++;
	}
	dup[i] = 0;
	return (dup);
}

int main()
{

	char str1[] = "Maisona";
	char *res = ft_strtrim(str1, "a");
	printf("%s\n", res);
	free (res);
}
