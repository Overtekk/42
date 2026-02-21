/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   scheduler_fifo.c                                   :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: roandrie <roandrie@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/02/17 09:30:39 by roandrie          #+#    #+#             */
/*   Updated: 2026/02/21 16:16:14 by roandrie         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "codexion.h"

static void	fifo_add_queue(t_data *data, t_coder *coder);

/**
 * Manages the FIFO scheduling for a coder.
 *
 * Locks the queue control mutex and performs the requested action:
 * either adding the coder to the waiting queue or removing it and
 * broadcasting a signal to wake up other waiting coders.
 */

int	scheduler_fifo(t_data *data, t_coder *coder, char *action)
{
	pthread_mutex_lock(&data->queue_control.lock);
	if (strcmp(action, ADD_QUEUE) == 0)
	{
		fifo_add_queue(data, coder);
	}
	else if (strcmp(action, REMOVE_QUEUE) == 0)
	{
		remove_from_queue(&data->queue_control);
		pthread_cond_broadcast(&data->queue_control.cond);
	}
	pthread_mutex_unlock(&data->queue_control.lock);
	return (0);
}

/**
 * Adds a coder to the FIFO queue and waits for its turn.
 *
 * The coder is added to the linked list. It then waits until it is the
 * first in line AND successfully takes both dongles. Uses a condition
 * variable for sleeping if it is first but dongles are currently unavailable.
 */

static void	fifo_add_queue(t_data *data, t_coder *coder)
{
	add_to_queue(&data->queue_control, coder);
	while (get_simulation(data) == 1
		&& (data->queue_control.first->coder != coder
			|| take_dongle(coder) == 1))
	{
		if (get_simulation(data) == 1
			&& data->queue_control.first->coder == coder)
		{
			pthread_mutex_unlock(&data->queue_control.lock);
			usleep(1000);
			pthread_mutex_lock(&data->queue_control.lock);
		}
		else
			pthread_cond_wait(&data->queue_control.cond,
				&data->queue_control.lock);
	}
}
