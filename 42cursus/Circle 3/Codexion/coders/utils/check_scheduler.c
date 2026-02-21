/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   check_scheduler.c                                  :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: roandrie <roandrie@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/02/20 11:08:50 by roandrie          #+#    #+#             */
/*   Updated: 2026/02/21 15:50:37 by roandrie         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "codexion.h"

/**
 * Check if the scheduler used is 'fifo'. If that the case, return '1' (True),
 * otherwise return '0' (False).
 */

int	is_fifo(t_data *data)
{
	if (strcmp(FIFO, data->scheduler) == 0)
		return (1);
	return (0);
}
