/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   main.c                                             :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: roandrie <roandrie@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/12 13:10:55 by roandrie          #+#    #+#             */
/*   Updated: 2025/11/29 13:50:22 by roandrie         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "../include/so_long.h"

static	int	check_filename(char *file_name)
{
	size_t	len;

	len = ft_strlen(file_name);
	if (len <= 4)
		return (ft_print_error(RED"Error\nFilename is too short\n"), 1);
	file_name = file_name + (len - 4);
	if (ft_strncmp(file_name, ".ber", 4) != 0)
	{
		ft_print_error(RED"Error\nWrong filename extension (need .ber)\n");
		return (1);
	}
	return (0);
}

static	int	init(char **argv, t_game *game)
{
	if (init_map(argv[1], game) == 0)
	{
		print_map_debug(game);
		if (check_map(game) == 0)
		{
			ft_printf(1, GRN"Map ok\n"R);
			init_game(game);
		}
	}
	free_memory(game);
	return (0);
}

int	main(int argc, char **argv)
{
	t_game	*game;

	if (argc != 2)
	{
		if (argc > 2)
			return (ft_print_error(RED"Error\nToo many arguments.\n"), 1);
		if (argc < 2)
			return (ft_print_error(RED"Error\nMissing map argument.\n"), 1);
	}
	if (check_filename(argv[1]) != 0)
		return (1);
	game = ft_calloc(1, sizeof(t_game));
	if (game == NULL)
	{
		free_memory(game);
		return (ft_print_error(RED"Error\nMalloc for game failed.\n"), 1);
	}
	init(argv, game);
	free (game);
	return (0);
}
