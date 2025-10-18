#include <unistd.h>

void ft_putchar(char c)
{
    write(1, &c, 1);
}

void ft_putstr(char *str)
{
    int i = 0;

    while (str[i])
    {
        ft_putchar(&str[i]);
        i++;
    }
}

int main(int argc, char *argv[])
{
    int i = 1;
    while (i < argc)
    {
        ft_putchar(argv[i]);
        ft_putchar('\n');
        i++;
    }
    return (0);
}