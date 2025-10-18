/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   rush01.c                                           :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: roandrie <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/07/13 14:30:05 by roandrie          #+#    #+#             */
/*   Updated: 2025/07/13 14:30:08 by roandrie         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <unistd.h>

void	ft_putchar(char c);
void	selectline(int lin, int col, int x, int y);
void	first_line(int col, int x);
void	last_line(int col, int x);
void	middle_line(int col, int x);

void	rush(int x, int y)
{
	int	lin;
	int	col;

	lin = 1;
	if (x > 0 && y > 0)
	{
		while (lin <= y)
		{
			col = 1;
			while (col <= x)
			{
				selectline(lin, col, x, y);
				col++;
			}
			ft_putchar('\n');
			lin++;
		}
	}
	else
	{
		write(1, "Comment tu veux créer une ", 27);
		write(1, "case avec un 0 ou un négatif???", 32);
	}
}

void	selectline(int lin, int col, int x, int y)
{
	if (lin == 1)
	{
		first_line(col, x);
	}
	else if (lin == y)
	{
		last_line(col, x);
	}
	else
	{
		middle_line(col, x);
	}
}

void	first_line(int col, int x)
{
	if (col == 1)
	{
		ft_putchar('/');
	}
	else if (col == x)
	{
		ft_putchar('\\');
	}
	else
	{
		ft_putchar('*');
	}
}

void	last_line(int col, int x)
{
	if (col == 1)
	{
		ft_putchar('\\');
	}
	else if (col == x)
	{
		ft_putchar('/');
	}
	else
	{
		ft_putchar('*');
	}
}

void	middle_line(int col, int x)
{
	if (col == 1 || col == x)
	{
		ft_putchar('*');
	}
	else
	{
		ft_putchar(' ');
	}
}
