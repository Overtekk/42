/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   rush04.c                                           :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: ydalmas <ydalmas@student.42.fr>            +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/07/12 09:34:51 by roandrie          #+#    #+#             */
/*   Updated: 2025/07/13 17:00:22 by ydalmas          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <unistd.h>

void	ft_putchar(char c);
void	centre(int j, int y, int x, int i);
void	ligne_cadre(int i, int y);
void	ft_on(int i, int y);
void	ft_under(int i, int y);

void	rush(int x, int y)
{
	int	i;
	int	j;

	i = 1;
	if (x <= 0 || y <= 0)
	{
		write(1, "Comment tu veux créer une ", 27);
		write(1, "case avec un 0 ou un négatif???", 32);
	}
	else
	{
		while (i <= y)
		{
			j = 1;
			while (j <= x)
			{
				centre(j, y, x, i);
				j++;
			}
			ft_putchar('\n');
			i++;
		}
	}
}

void	centre(int j, int y, int x, int i)
{
	if (j == 1)
		ft_on(i, y);
	else if (j == x)
		ft_under(i, y);
	else
		ligne_cadre(i, y);
}

void	ligne_cadre(int i, int y)
{
	if (i == 1 || i == y)
		ft_putchar('B');
	else
		ft_putchar(' ');
}

void	ft_on(int i, int y)
{
	if (i == 1)
		ft_putchar('A');
	else if (i == y)
		ft_putchar('C');
	else
		ft_putchar('B');
}

void	ft_under(int i, int y)
{
	if (i == 1)
		ft_putchar('C');
	else if (i == y)
		ft_putchar('A');
	else
		ft_putchar('B');
}
