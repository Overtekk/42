/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   setter.c                                           :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: roandrie <roandrie@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/02/11 13:53:16 by roandrie          #+#    #+#             */
/*   Updated: 2026/02/21 15:47:31 by roandrie         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "codexion.h"

/**
 * Setter for the burnout timer for a specific coder.
 * Protected by a mutex to prevent data-race and duplicating variable.
 */

void	set_burnout(t_coder *coder)
{
	pthread_mutex_lock(&coder->mutex_burnout);
	coder->time_bournout = get_time_ms();
	pthread_mutex_unlock(&coder->mutex_burnout);
}

/**
 * Setter for a specific coder if he have completed all requieres compilation.
 * Protected by a mutex to prevent data-race and duplicating variable.
 */

void	set_finished(t_coder *coder)
{
	pthread_mutex_lock(&coder->mutex_finish);
	coder->have_finished = 1;
	pthread_mutex_unlock(&coder->mutex_finish);
}
