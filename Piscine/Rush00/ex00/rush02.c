/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   rush01.c                                           :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: npillet <npillet@student.42.fr>            +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/07/13 13:34:57 by npillet           #+#    #+#             */
/*   Updated: 2025/07/13 14:28:21 by npillet          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <unistd.h>

void	ft_putchar(char c);
void	cadre(int j, int x, int i, int y);
void	ligne_cadre(int i, int y);

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
				cadre(j, x, i, y);
				j++;
			}
			ft_putchar('\n');
			i++;
		}
	}
}

void	cadre(int j, int x, int i, int y)
{
	if (j == 1 || j == x)
	{
		if (i == 1)
			ft_putchar('A');
		else if (i == y)
			ft_putchar('C');
		else
			ft_putchar('B');
	}
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
