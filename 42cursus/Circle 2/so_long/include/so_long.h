/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   so_long.h                                          :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: roandrie <roandrie@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/12 09:49:47 by roandrie          #+#    #+#             */
/*   Updated: 2025/11/12 16:58:31 by roandrie         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#ifndef SO_LONG_H
# define SO_LONG_H

//*LIBFT HEADER*//
# include "../libft/include/ft_printf.h"
# include "../libft/include/get_next_line.h"
# include "../libft/include/libft.h"

//*MINILIBX HEADER*//
# include "../minilibx-linux/mlx_int.h"
# include "../minilibx-linux/mlx.h"

//*LIBRARY*//
#include "unistd.h"
#include <fcntl.h>

//*STRUCTURE*//
typedef struct s_map
{
	int		x_map;
	int		y_map;
}	t_map;

typedef struct s_game
{
	struct s_map	map;
}	t_game;

//*PROTYPE*//
int	ft_print_error(char *err_msg);

#endif
