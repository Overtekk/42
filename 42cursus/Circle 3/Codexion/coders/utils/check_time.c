/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   check_time.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: roandrie <roandrie@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/02/07 15:23:48 by roandrie          #+#    #+#             */
/*   Updated: 2026/02/21 15:49:47 by roandrie         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "codexion.h"

/**
 * Gets the current absolute time in milliseconds.
 *
 * Retrieves the system's current time using gettimeofday and converts the
 * seconds and microseconds into a single milliseconds value. Then return the
 * current time in milliseconds.
 */

long long	get_time_ms(void)
{
	struct timeval	tv;

	gettimeofday(&tv, NULL);
	return ((tv.tv_sec * 1000) + (tv.tv_usec / 1000));
}

/**
 * Compares the current system time with the recorded start time in the data
 * structure to determine how much time has passed. This is used to timestamp
 * the logs accurately.
 */

long long	get_sim_time(t_data *data)
{
	return (get_time_ms() - data->start_time);
}
