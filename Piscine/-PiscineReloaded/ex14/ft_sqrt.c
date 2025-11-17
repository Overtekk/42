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

int ft_sqrt(int nb)
{
	int	mult;

	mult = 1;
	if (nb < 0)
		return (0);
	while ((mult * mult) <= nb && mult < 46340)
	{
		if ((mult * mult) == nb)
			return (mult);
		mult++;
	}
	return (0);

}

int main(int argc, char *argv[])
{
    if (argc == 2)
    {
        int nb = atoi(argv[1]);
        printf("%d\n", ft_sqrt(nb));
    }
    else
        ft_putstr("Error. 1 arguments needed\n");
    return (0);
}