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

void ft_div_mod(int a, int b, int *div, int *mod)
{
    *div = a / b;
    *mod = a % b;
}

int main(int argc, char *argv[])
{
    if (argc == 3)
    {
        int a = atoi(argv[1]);
        int b = atoi(argv[2]);
        int div = 0;
        int mod = 0;
        ft_div_mod(a, b, &div, &mod);
        printf("Div = %d et Mod = %d\n", div, mod);
    }
    else
        ft_putstr("Error. 3 arguments needed\n");
    return (0);
}