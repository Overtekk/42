/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   so_long.h                                          :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: roandrie <roandrie@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/12 09:49:47 by roandrie          #+#    #+#             */
/*   Updated: 2025/11/20 12:36:39 by roandrie         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#ifndef SO_LONG_H
# define SO_LONG_H

//#COLORS#//
# define RED "\e[1;91m"
# define GRN "\e[1;92m"
# define R "\e[0m"

//#LIBFT HEADER#//
# include "../libft/include/libft.h"
//#MINILIBX HEADER#//
# include "../minilibx-linux/mlx.h"

//#LIBRARY#//
# include <unistd.h>
# include <stdlib.h>
# include <fcntl.h>

//#STRUCTURE#//

typedef struct s_coord
{
	int	x;
	int	y;
}		t_coord;

typedef struct s_map
{
	char	**grid;
	int		x;
	int		y;
	int		error_south;
	int		error_north;
	int		error_east;
	int		error_west;
	t_coord	player;
}			t_map;

typedef struct s_path_check
{
	int	collectibles_found;
	int	exit_reached;
}		t_path_check;

typedef struct s_game
{
	t_map	map;
	int		character;
	int		collectible;
	int		exit;
}			t_game;

//#FUNCTIONS#//
int		init_map(char *argv, t_game *game);
int		check_map(t_game *game);
int		is_valid_path(t_game *game);

void	ft_print_error(char *err_msg);
void	map_error(t_game *game);

void	free_memory(t_game *game);
void	free_memory_path(char **tab, t_game *game);
void	free_map_list(char *line, t_list *map_list);

void	print_map_debug(t_game *game);

#endif
