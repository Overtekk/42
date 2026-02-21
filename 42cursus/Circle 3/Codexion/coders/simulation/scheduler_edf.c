/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   scheduler_edf.c                                    :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: roandrie <roandrie@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/02/20 10:40:41 by roandrie          #+#    #+#             */
/*   Updated: 2026/02/21 16:20:11 by roandrie         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "codexion.h"

static int	is_priority(t_data *data, t_coder *coder);

/**
 * Adds a coder to the EDF scheduling system.
 *
 * Pushes the coder into the min-heap priority queue. The thread then waits
 * until it gains local priority over its neighbors to take the dongles.
 * Once successful, it removes itself from the heap.
 */

void	scheduler_edf_add(t_data *data, t_coder *coder)
{
	t_heap	*controler;

	controler = &data->heap_control;
	pthread_mutex_lock(&controler->lock);
	heap_push(controler, coder);
	pthread_cond_broadcast(&controler->cond);
	pthread_mutex_unlock(&controler->lock);
	while (get_simulation(data) == 1)
	{
		if (is_priority(data, coder))
		{
			if (take_dongle(coder) == 0)
				break ;
		}
		usleep(500);
	}
	pthread_mutex_lock(&controler->lock);
	heap_pop(controler, coder);
	pthread_cond_broadcast(&controler->cond);
	pthread_mutex_unlock(&controler->lock);
}

/**
 * Checks if the coder has priority over its immediate neighbors.
 *
 * Evaluates the burnout deadlines of the current coder and its left/right
 * neighbors. If a neighbor has an earlier deadline, priority is denied to
 * allow the neighbor to go first and prevent burnout.
 */

static int	is_priority(t_data *data, t_coder *coder)
{
	int			left_idx;
	int			right_idx;
	long long	my_time;

	left_idx = (coder->id - 2 + data->nbr_coders) % data->nbr_coders;
	right_idx = coder->id % data->nbr_coders;
	my_time = get_burnout(coder);
	if (get_burnout(&data->coder[left_idx]) < my_time)
		return (0);
	if (get_burnout(&data->coder[right_idx]) < my_time)
		return (0);
	return (1);
}
