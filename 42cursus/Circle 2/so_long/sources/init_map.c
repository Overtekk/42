/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   init_map.c                                         :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: roandrie <roandrie@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/13 16:13:21 by roandrie          #+#    #+#             */
/*   Updated: 2025/11/15 21:04:07 by roandrie         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "../include/so_long.h"

void	print_map_debug(t_game *game)
{
	int	y;

	y = 0;
	ft_printf("\nShowing Map\n");
	while (game->map.grid[y] != NULL)
	{
		ft_putstr_fd(game->map.grid[y], 1);
		ft_putchar_fd('\n', 1);
		y++;
	}
}

static	int	convert_map(t_list *map_list, t_game *game)
{
	int		y;
	t_list	*temp;

	if (map_list == NULL)
		return (ft_print_error("Error\nMap is empty.\n"));
	game->map.y = ft_lstsize(map_list);
	game->map.x = ft_strlen(map_list->content);
	game->map.grid = malloc(sizeof(char *) * (game->map.y + 1));
	if (game->map.grid == NULL)
		return (ft_print_error("Error\nMalloc failed for grid.\n"));
	y = 0;
	temp = map_list;
	while (temp)
	{
		game->map.grid[y] = ft_strdup(temp->content);
		if (game->map.grid[y] == NULL)
		{
			return (ft_print_error("Error\nMalloc failes for grid row.\n"));
		}
		temp = temp->next;
		y++;
	}
	game->map.grid[y] = NULL;
	return (0);
}

int	init_map(char *map_file, t_game *game)
{
	int			map_fd;
	char		*line;
	t_list		*map_list;
	t_list		*new_node_map;

	map_list = NULL;
	map_fd = open(map_file, O_RDONLY);
	if (map_fd < 0)
		return (ft_print_error("Error\nOpening map failed.\n"));
	while (1)
	{
		line = get_next_line(map_fd);
		if (line == NULL)
			break;
		new_node_map = ft_lstnew(line);
		if (new_node_map == NULL)
		{
			free (line);
			ft_lstclear(&map_list, free);
			return (ft_print_error("Error\nMalloc failed while reading line.\n"));
		}
		ft_lstadd_back(&map_list, new_node_map);
	}
	close (map_fd);
	if (convert_map(map_list, game) != 0)
	{
		ft_lstclear(&map_list, free);
		return (2);
	}
	ft_lstclear(&map_list, free);
	return (0);
}
