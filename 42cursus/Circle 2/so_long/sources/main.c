/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   main.c                                             :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: roandrie <roandrie@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/12 13:10:55 by roandrie          #+#    #+#             */
/*   Updated: 2025/11/15 23:20:41 by roandrie         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "../include/so_long.h"

static	int	check_filename(char *file_name)
{
	file_name = file_name + (ft_strlen(file_name) - 4);
	if (ft_strncmp(file_name, ".ber", 4) != 0)
	{
		ft_print_error("Error\nWrong filename extension (need .ber)\n");
		return (1);
	}
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
	if (check_filename(argv[1]) != 0)
		return (1);
	game = malloc(sizeof(t_game));
	if (game == NULL)
	{
		free_memory(game);
		return (ft_print_error("Error\nMalloc for game failed.\n"));
	}
	if (init_map(argv[1], game) == 0 && check_map(game) == 0)
		ft_printf("ok");
	free_memory(game);
	return (0);
}
