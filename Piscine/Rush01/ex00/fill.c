/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   fill.c                                             :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: vilecali <vilecali@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/07/20 20:26:14 by vilecali          #+#    #+#             */
/*   Updated: 2025/07/20 21:56:24 by vilecali         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <unistd.h>

int	is_valid(int grid[4][4], int argvi[4][4]);

void	ft_putchar( char c)
{
	write (1, &c, 1);
}

void	affichage(int grid[4][4])
{
	int	i;
	int	y;

	i = 0;
	y = 0;
	while (y < 4)
	{
		while (i < 4)
		{
			ft_putchar(grid[y][i] + '0');
			i++;
		}
		ft_putchar('\n');
		y++;
		i = 0;
	}
}

int	verif_doublon(int grid[4][4], int x, int y, int change)
{
	int	i;

	i = 0;
	while (i < x)
	{
		if (grid[i][y] == change)
			return (0);
		i++;
	}
	i = 0;
	while (i < y)
	{
		if (grid[x][i] == change)
			return (0);
		i++;
	}
	return (1);
}

int	fill(int grid[4][4], int x, int y, int argvi[4][4])
{
	int	i;

	i = 1;
	if ((x == 3 && y == 4))
		return (is_valid (grid, argvi));
	if (y == 4)
	{
		y = 0;
		x++;
	}
	while (i < 5)
	{
		grid[x][y] = i;
		if (verif_doublon(grid, x, y, i))
			if (fill(grid, x, y + 1, argvi))
				return (1);
		i++;
	}
	return (0);
}
