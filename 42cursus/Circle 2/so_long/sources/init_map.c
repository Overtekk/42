/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   init_map.c                                         :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: roandrie <roandrie@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/13 16:13:21 by roandrie          #+#    #+#             */
/*   Updated: 2025/11/15 22:39:52 by roandrie         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "../include/so_long.h"

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
		return (ft_print_error("Error\nMalloc failed for grid y.\n"));
	y = 0;
	temp = map_list;
	while (temp)
	{
		game->map.grid[y] = ft_strdup(temp->content);
		if (game->map.grid[y] == NULL)
			return (free_memory(game), 1);
		temp = temp->next;
		y++;
	}
	game->map.grid[y] = NULL;
	return (0);
}

static	char	*get_line(char *line, int map_fd)
{
	char *line_copy;

	line = get_next_line(map_fd);
	line_copy = ft_strtrim(line, "\n");
	free (line);
	return (line_copy);
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
		line = get_line(line, map_fd);
		if (line == NULL)
			break;
		new_node_map = ft_lstnew(line);
		if (new_node_map == NULL)
			return (free_map_list(line, map_list));
		ft_lstadd_back(&map_list, new_node_map);
	}
	close (map_fd);
	if (convert_map(map_list, game) != 0)
		return (free_map_list(line, map_list));
	ft_lstclear(&map_list, free);
	check_map(game);
	return (0);
}
