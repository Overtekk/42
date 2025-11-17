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

void ft_swap(int *a, int *b)
{
    int temp;
    temp = *a;
    *a = *b;
    *b = temp;
}

int main(int argc, char *argv[])
{
    if (argc == 3)
    {
        int nbr1, nbr2;
        nbr1 = atoi(argv[1]);
        nbr2 = atoi(argv[2]);
        ft_swap(&nbr1, &nbr2);
        printf("%d %d\n", nbr1, nbr2);
    }
    else
        ft_putstr("Only 2 argument\n");
    return (0);
}
