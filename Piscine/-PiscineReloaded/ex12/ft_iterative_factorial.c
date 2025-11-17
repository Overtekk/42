#include <unistd.h>
#include <stdlib.h>
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

int ft_iterative_factorial(int nb)
{
    int result = 1;

    if (nb < 0)
        return (0);
    if (nb == 0)
        return (1);
    while (nb > 0)
    {
        result *= nb;
        nb--;
    }
    return (result);
}

int main(int argc, char *argv[])
{
    if (argc == 2)
    {
        int nb = atoi(argv[1]);
        printf("%d\n", ft_iterative_factorial(nb));
    }
    else
        ft_putstr("Error. 1 argument needed\n");
    return (0);
}