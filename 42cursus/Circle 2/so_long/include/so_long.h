/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   so_long.h                                          :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: roandrie <roandrie@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/12 09:49:47 by roandrie          #+#    #+#             */
/*   Updated: 2025/11/27 12:12:23 by roandrie         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#ifndef SO_LONG_H
# define SO_LONG_H

//#COLORS#//
# define RED 	"\e[1;91m"
# define GRN 	"\e[1;92m"
# define B		"\e[1;94m"
# define R		"\e[0m"

	//#LIBRARY#//
# include <unistd.h>
# include <stdlib.h>
# include <fcntl.h>
# include <stdio.h>
# include <string.h>
# include <X11/X.h>
# include <X11/keysym.h>
# include "../libft/include/libft.h"
# include "../minilibx-linux/mlx.h"

	//#KEYS#//
# define KEY_ESC		65307
# define KEY_W			119
# define KEY_A			97
# define KEY_S			115
# define KEY_D			100

	//#STRUCTURE#//
//Sprite//
typedef struct s_sprite
{
	void	*wall;
	void	*floor;
	void	*player;
	void	*collectible;
	void	*exit_close;
	int		width;
	int		height;
}			t_sprite;

//Player coordinates//
typedef struct s_coord
{
	int	x;
	int	y;
}		t_coord;

//Structure for map//
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
	int		c_found;
	int		exit_reached;
}			t_map;

//Structure for the game//
typedef struct s_game
{
	t_map		map;
	int			character;
	int			collectible;
	int			exit;
	t_sprite	sprite;
	void		*mlx;
	void		*screen;
}				t_game;

	//#FUNCTIONS#//
//Check if map is valid//
int		init_map(char *argv, t_game *game);
int		check_map(t_game *game);
int		is_valid_path(t_game *game);

//Game relative functions//
int		init_game(t_game *game);
int		stop_game(t_game *game);
int		close_game(t_game *game);

int		key_press(int keycode, t_game *game);

void	print_img(t_game *game, void *img, int x, int y);
int		set_img(t_game *game);
void	draw_map(t_game *game);
int		check_img_error(t_game *game);

//Error gestion//
void	ft_print_error(char *err_msg);
void	map_error(t_game *game);
void	path_error(t_game *game);

//Memory gestion//
void	free_memory(t_game *game);
void	free_memory_path(char **tab);
void	free_map_list(char *line, t_list *map_list);

//Debug fonction//
void	print_map_debug(t_game *game);
void	print_map_copy_debug(char **tab);

#endif
