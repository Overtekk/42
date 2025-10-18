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

void ft_ft(int *nbr)
{
    *nbr = 42;
}

int main(int argc, char *argv[])
{
    if (argc == 2)
    {
        int nbr = atoi(argv[1]);
        ft_ft(&nbr);
        printf("%d\n", nbr);
    }
    else
        ft_putstr("Only 1 argument\n");
    return (0);
}