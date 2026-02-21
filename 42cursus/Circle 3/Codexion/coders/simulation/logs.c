/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   logs.c                                             :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: roandrie <roandrie@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/02/10 15:03:58 by roandrie          #+#    #+#             */
/*   Updated: 2026/02/21 16:21:41 by roandrie         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "codexion.h"

/**
 * Print each action from a coder in the log in a specific format:
 * timestamp_im_ms "coder" "action"
 * Protected with a mutex to prevent mixed logs.
 */

void	print_logs(int index, char *dongle_id, char *action, t_data *data)
{
	long long	time;

	pthread_mutex_lock(&data->mutex_print);
	time = get_time_ms() - data->start_time;
	if (strcmp(action, ACT_TAKE) == 0)
		printf(LOG_TAKE_DONGLE, time, index, dongle_id);
	else if (strcmp(action, ACT_COMP) == 0)
		printf(LOG_COMPILING, time, index,
			data->coder[index - 1].code_compiled + 1);
	else if (strcmp(action, ACT_DEBUG) == 0)
		printf(LOG_DEBUGGING, time, index);
	else if (strcmp(action, ACT_REFAC) == 0)
		printf(LOG_REFACTOR, time, index);
	else if (strcmp(action, ACT_BURNS) == 0)
		printf(LOG_BURNS_OUT, time, index);
	pthread_mutex_unlock(&data->mutex_print);
}
