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
        ft_putchar(str[i]);
        i++;
    }
}

int main(int argc, char *argv[])
{
    if (argc == 2)
    {
        char *str = argv[1];
        ft_putstr(str);
        ft_putchar('\n');
    }
    else
        ft_putstr("Error. 1 arguments needed\n");
    return (0);
}