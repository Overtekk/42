/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   main.c                                             :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: roandrie <roandrie@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/12 13:10:55 by roandrie          #+#    #+#             */
/*   Updated: 2025/11/13 16:16:59 by roandrie         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "../include/so_long.h"

static	int	check_filename(char *file_name)
{
	file_name = file_name + (ft_strlen(file_name) - 4);
	if (ft_strncmp(file_name, ".ber", 4))
		ft_print_error("Error\nWrong filename extension (need .ber)\n");
	return (0);
}

int	main(int argc, char **argv)
{
	t_game	*game;

	if (argc != 2)
	{
		if (argc > 2)
			return (ft_print_error("Error\nToo many arguments.\n"));
		if (argc < 2)
			return (ft_print_error("Error\nPlease, but the map argument.\n"));
	}
	check_filename(argv[1]);
	game = malloc(sizeof(t_game));
	init_map(argv[1], game);
	free_memory(game);
	return (0);
}
