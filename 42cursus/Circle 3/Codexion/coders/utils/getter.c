/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   getter.c                                           :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: roandrie <roandrie@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/02/11 13:37:03 by roandrie          #+#    #+#             */
/*   Updated: 2026/02/23 15:20:41 by roandrie         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "codexion.h"

/**
 * Getter function to know if the simulation is activate or not.
 * Protected by a mutex to prevent data-race.
 */

int	get_simulation(t_data *data)
{
	int	status;

	status = 0;
	pthread_mutex_lock(&data->mutex_simu);
	status = data->simulation_active;
	pthread_mutex_unlock(&data->mutex_simu);
	return (status);
}

/**
 * Getter function to retrieve the timestamp at which a coder will burn out.
 * Protected by a mutex to prevent data-race.
 */

long long	get_burnout(t_coder *coder)
{
	long long	burnout;

	burnout = 0;
	pthread_mutex_lock(&coder->mutex_burnout);
	burnout = coder->time_bournout;
	pthread_mutex_unlock(&coder->mutex_burnout);
	return (burnout);
}

/**
 * Getter function to check if a coder has reached the required number of
 * compilations.
 * Protected by a mutex to prevent data-race.
 */

int	get_have_finished(t_coder *coder)
{
	int	finished;

	finished = 0;
	pthread_mutex_lock(&coder->mutex_finish);
	finished = coder->have_finished;
	pthread_mutex_unlock(&coder->mutex_finish);
	return (finished);
}
