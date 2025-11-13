/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   init_map.c                                         :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: roandrie <roandrie@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/13 16:13:21 by roandrie          #+#    #+#             */
/*   Updated: 2025/11/13 16:18:09 by roandrie         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "../include/so_long.h"

int	init_map(char *argv, t_game *game)
{
	int	map_fd;

	map_fd = open(argv, O_RDONLY);
	if (map_fd < 0)
	{
		return (ft_print_error("Error\nOpening map failed.\n"));
		return (1);
	}
	close (map_fd);
	return (0);
}
