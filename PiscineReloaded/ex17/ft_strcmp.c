#include <unistd.h>
#include <stdio.h>

void ft_putstr(char *str)
{
    int i = 0;

    while (str[i])
    {
        write(1, &str[i], 1);
        i++;
    }
}

int ft_strcmp(char *s1, char *s2)
{
    int i = 0;
	while (s1[i] && s2[i] && s1[i] == s2[i])
		i++;
	return (s1[i] - s2[i]);
}

int main(int argc, char *argv[])
{
    if (argc == 3)
    {
        char *s1 = argv[1];
        char *s2 = argv[2];
        printf("%d\n", ft_strcmp(s1, s2));
    }
    else
        ft_putstr("Error. 2 arguments needed\n");
    return (0);
}