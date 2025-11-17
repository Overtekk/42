#include <unistd.h>
#include <stdlib.h>

void ft_putchar(char c)
{
    write(1, &c, 1);
}

void ft_putstr(char *str)
{
    int i = 0;

    while (str[i])
    {
        write(1, &str[i], 1);
        i++;
    }
}

void ft_is_negative(int n)
{
    if (n >= 0)
        ft_putchar('P');
    else
        ft_putchar('N');
}

int main(int argc, char *argv[])
{
    if (argc == 2)
    {
        int nbr = atoi(argv[1]);
        ft_is_negative(nbr);
    }
    else
        ft_putstr("Only 1 argument\n");
    return (0);
}