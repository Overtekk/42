/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   getter.c                                           :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: roandrie <roandrie@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/02/11 13:37:03 by roandrie          #+#    #+#             */
/*   Updated: 2026/02/11 13:58:58 by roandrie         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "codexion.h"

int	get_simulation(t_data *data)
{
	int	status;

	status = 0;
	pthread_mutex_lock(&data->mutex_simu);
	status = data->simulation_active;
	pthread_mutex_unlock(&data->mutex_simu);
	return (status);
}

long long	get_burnout(t_coder *coder)
{
	long long	burnout;

	burnout = 0;
	pthread_mutex_lock(&coder->mutex_burnout);
	burnout = coder->time_bournout;
	pthread_mutex_unlock(&coder->mutex_burnout);
	return (burnout);
}
