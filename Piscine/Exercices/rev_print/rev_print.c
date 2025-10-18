#include <unistd.h>
#include <stdio.h>

int ft_strlen(char *str)
{
    int i = 0;
    while (str[i] != '\0')
    {
        i++;
    }
    return (i);
}

char    ft_rev_print(char *str)
{
    int size;
    size = ft_strlen(str) - 1;
    while (size >= 0)
    {
        write(1, &str[size], 1);
        size--;
    }
    return (*str);
}

int main(void)
{
    char str[] = "Bonjour";
    ft_rev_print(str);
}