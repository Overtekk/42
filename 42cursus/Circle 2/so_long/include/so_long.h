/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   so_long.h                                          :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: roandrie <roandrie@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/12 09:49:47 by roandrie          #+#    #+#             */
/*   Updated: 2025/11/13 15:29:21 by roandrie         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#ifndef SO_LONG_H
# define SO_LONG_H

//#LIBFT HEADER#//
# include "../libft/include/libft.h"
//#MINILIBX HEADER#//
# include "../minilibx-linux/mlx.h"

//#LIBRARY#//
# include "unistd.h"
# include "fcntl.h"

//#STRUCTURE#//
typedef struct s_map
{
	int		**map;
	int		x;
	int		y;
}	t_map;

typedef struct s_game
{
	int				character;
	int				item;
	int				exit;
	struct s_map	**map;
}	t_game;

//#PROTYPE#//
int	is_valid_map(char *argv);

int	ft_print_error(char *err_msg);

#endif
