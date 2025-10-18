#include <unistd.h>

void ft_putchar(char c)
{
    write(1, &c, 1);
}

void ft_print_numbers(void)
{
    char nbr;
    nbr = '0';

    while (nbr <= '9')
    {
        ft_putchar(nbr);
        nbr++;
    }
}

int main(void)
{
    ft_print_numbers();
}