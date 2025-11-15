/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   so_long.h                                          :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: roandrie <roandrie@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/12 09:49:47 by roandrie          #+#    #+#             */
/*   Updated: 2025/11/15 20:54:03 by roandrie         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#ifndef SO_LONG_H
# define SO_LONG_H

//#LIBFT HEADER#//
# include "../libft/include/libft.h"
//#MINILIBX HEADER#//
# include "../minilibx-linux/mlx.h"

//#LIBRARY#//
# include <unistd.h>
# include <stdlib.h>
# include <fcntl.h>

//#STRUCTURE#//
typedef struct s_map
{
	char	**grid;
	int		x;
	int		y;
}	t_map;

typedef struct s_game
{
	t_map	map;
}	t_game;

//#PROTYPE#//
int		init_map(char *argv, t_game *game);

void	free_memory(t_game *game);

void	print_map_debug(t_game *game);
int		ft_print_error(char *err_msg);

#endif
