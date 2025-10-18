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

int ft_strlen(char *str)
{
    int i = 0;
    
    while (str[i])
    {
        i++;
    }
    return (i);
}

int main(int argc, char *argv[])
{
    if (argc == 2)
    {
        char *str = argv[1];
        printf("%d\n", ft_strlen(str));
    }
    else
        ft_putstr("Error. 1 arguments needed\n");
    return (0);
}