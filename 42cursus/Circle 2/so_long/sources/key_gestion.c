/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   key_gestion.c                                      :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: roandrie <roandrie@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/27 09:17:56 by roandrie          #+#    #+#             */
/*   Updated: 2025/11/27 12:10:26 by roandrie         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "../include/so_long.h"

int	key_press(int keycode, t_game *game)
{
	if (keycode == KEY_ESC)
	{
		ft_printf(RED"Game closed\n"R);
		close_game(game);
	}
	return (0);
}
