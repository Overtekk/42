/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   destroy.c                                          :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: roandrie <roandrie@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/02/16 16:35:21 by roandrie          #+#    #+#             */
/*   Updated: 2026/02/21 15:53:58 by roandrie         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "codexion.h"

static void	destroy_mutex_cond(t_data *data);

void	destroy_mutex(t_data *data)
{
	int	index;

	index = 0;
	while (index != data->nbr_coders)
	{
		pthread_mutex_destroy(&data->dongle[index].lock);
		pthread_mutex_destroy(&data->coder[index].mutex_burnout);
		pthread_mutex_destroy(&data->coder[index].mutex_finish);
		index++;
	}
	pthread_mutex_destroy(&data->mutex_print);
	pthread_mutex_destroy(&data->mutex_simu);
	pthread_mutex_destroy(&data->queue_control.lock);
	pthread_mutex_destroy(&data->heap_control.lock);
	destroy_mutex_cond(data);
}

static void	destroy_mutex_cond(t_data *data)
{
	pthread_cond_destroy(&data->queue_control.cond);
	pthread_cond_destroy(&data->heap_control.cond);
}
