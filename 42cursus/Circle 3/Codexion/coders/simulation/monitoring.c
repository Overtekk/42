/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   monitoring.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: roandrie <roandrie@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/02/07 15:37:16 by roandrie          #+#    #+#             */
/*   Updated: 2026/02/27 10:26:38 by roandrie         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "codexion.h"

static int	check_burns_out(t_data *data, int *finish);
static void	stop_simulation(t_data *data);

/**
 * Function used by the monitoring thread. It check the burnout of each coder
 * and stop the simulation if a coder has burnout, or if all coders have
 * compiled the number of time requiered.
 */

void	*monitoring_simulation(void *arg)
{
	t_data	*data;
	int		finish;

	data = (t_data *)arg;
	while (get_simulation(data) == 1)
	{
		if (check_burns_out(data, &finish) == 1)
			return (NULL);
		if (finish == data->nbr_coders)
		{
			stop_simulation(data);
			pthread_mutex_lock(&data->mutex_print);
			printf(LOG_SUCCESS "\n");
			pthread_mutex_unlock(&data->mutex_print);
			return (NULL);
		}
		usleep(100);
	}
	return (NULL);
}

/**
 * Check each coder to know if they have burnout. If not, check the next.
 * Otherwise, stop the simulation, print the burnout in the log and return '1'.
 */

static int	check_burns_out(t_data *data, int *finish)
{
	int	index;

	index = 0;
	*finish = 0;
	while (data->nbr_coders != index)
	{
		if (get_have_finished(&data->coder[index]) == 1)
			(*finish)++;
		else if ((get_time_ms() - get_burnout(&data->coder[index]))
			> data->burnout_max)
		{
			stop_simulation(data);
			print_logs(data->coder[index].id, 0, ACT_BURNS, data);
			return (1);
		}
		index++;
	}
	return (0);
}

/**
 * Stop the simulation by setting the variable 'simulation active' to 0. Then,
 * send a broadcast to each queue to tell coder to quit it.
 * Protected by a mutex to prevent data-race.
 */

static void	stop_simulation(t_data *data)
{
	pthread_mutex_lock(&data->mutex_simu);
	data->simulation_active = 0;
	pthread_mutex_unlock(&data->mutex_simu);
	pthread_mutex_lock(&data->queue_control.lock);
	pthread_cond_broadcast(&data->queue_control.cond);
	pthread_mutex_unlock(&data->queue_control.lock);
	pthread_mutex_lock(&data->heap_control.lock);
	pthread_cond_broadcast(&data->heap_control.cond);
	pthread_mutex_unlock(&data->heap_control.lock);
}
