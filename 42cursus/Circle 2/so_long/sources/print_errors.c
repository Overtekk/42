/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_print_error.c                                   :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: roandrie <roandrie@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/12 15:23:01 by roandrie          #+#    #+#             */
/*   Updated: 2025/11/25 15:02:16 by roandrie         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "../include/so_long.h"

void	ft_print_error(char *err_msg)
{
	write(2, err_msg, ft_strlen(err_msg));
}

void	map_error(t_game *game)
{
	if (game->character > 1)
		ft_print_error(RED"Error\nToo many character.\n");
	else if (game->character == 0)
		ft_print_error(RED"Error\nMissing character.\n");
	if (game->exit > 1)
		ft_print_error(RED"Error\nToo many exit.\n");
	else if (game->exit == 0)
		ft_print_error(RED"Error\nMissing exit.\n");
	if (game->collectible == 0)
		ft_print_error(RED"Error\nMissing collectible.\n");
	if (game->map.error_north == 1)
		ft_print_error(RED"Error\nInvalid walls north.\n");
	if (game->map.error_south == 1)
		ft_print_error(RED"Error\nInvalid walls south.\n");
	if (game->map.error_east == 1)
		ft_print_error(RED"Error\nInvalid walls east.\n");
	if (game->map.error_west == 1)
		ft_print_error(RED"Error\nInvalid walls west.\n");
}

void	path_error(t_game *game)
{
	if (game->map.c_found != game->collectible)
		ft_print_error(RED"Error\nCannot collect all collectibles.\n");
	if (game->map.exit_reached != 1)
		ft_print_error(RED"Error\nExit is blocked.\n");
}
