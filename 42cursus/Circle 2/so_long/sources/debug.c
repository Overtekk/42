/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   debug.c                                            :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: roandrie <roandrie@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/15 23:19:32 by roandrie          #+#    #+#             */
/*   Updated: 2025/11/20 14:10:34 by roandrie         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "../include/so_long.h"

void	print_map_debug(t_game *game)
{
	int	y;

	y = 0;
	ft_printf(GRN"\n\n--Showing Map--\n"R);
	while (game->map.grid[y] != NULL)
	{
		ft_putstr_fd(game->map.grid[y], 1);
		ft_putchar_fd('\n', 1);
		y++;
	}
}

void	print_map_copy_debug(char **tab)
{
	int	y;

	y = 0;
	ft_printf(GRN"\n\n--Showing Copy Map--\n"R);
	while (tab[y] != NULL)
	{
		ft_putstr_fd(tab[y], 1);
		ft_putchar_fd('\n', 1);
		y++;
	}
}
