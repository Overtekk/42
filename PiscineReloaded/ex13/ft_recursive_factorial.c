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

int ft_recursive_factorial(int nb)
{
    if (nb < 0)
        return (0);
    else if (nb == 0)
        return (1);
    else
        return (nb * ft_recursive_factorial(nb - 1));
}

int main(int argc, char *argv[])
{
    if (argc == 2)
    {
        int nb = atoi(argv[1]);
        printf("%d\n", ft_recursive_factorial(nb));
    }
    else
        ft_putstr("Error. 1 argument needed\n");
    return (0);
}