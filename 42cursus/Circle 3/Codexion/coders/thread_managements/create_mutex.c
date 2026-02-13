/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   create_mutex.c                                     :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: roandrie <roandrie@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/02/06 16:42:31 by roandrie          #+#    #+#             */
/*   Updated: 2026/02/13 09:18:39 by roandrie         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "codexion.h"

int	init_mutex_for_dongle(t_data *data)
{
	int	index;

	index = 0;
	while (data->nbr_dongle != index)
	{
		pthread_mutex_init(&data->dongle[index].lock, NULL);
		pthread_mutex_init(&data->coder[index].mutex_burnout, NULL);
		index++;
	}
	return (0);
}

int	init_mutex_print(t_data *data)
{
	pthread_mutex_init(&data->mutex_print, NULL);
	pthread_mutex_init(&data->mutex_simu, NULL);
	pthread_mutex_init(&data->queue_control.lock, NULL);
	return (0);
}
