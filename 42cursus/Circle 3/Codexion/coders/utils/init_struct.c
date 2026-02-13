/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   init_struct.c                                      :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: roandrie <roandrie@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/02/11 10:46:33 by roandrie          #+#    #+#             */
/*   Updated: 2026/02/13 15:39:18 by roandrie         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "codexion.h"

static	void	create_coders_and_dongle(t_data *data);

int	init_struct(int *value, t_data *data)
{
	data->coder = calloc(1, sizeof(t_coder) * value[0]);
	if (data->coder == NULL)
		return (print_error(STR_ERR_MALLOC, NULL, data));
	data->dongle = calloc(1, sizeof(t_dongle) * value[0]);
	if (data->dongle == NULL)
		return (print_error(STR_ERR_MALLOC, NULL, data));
	data->nbr_coders = value[0];
	data->nbr_dongle = value[0];
	data->burnout_max = value[1];
	data->time_comp = value[2];
	data->time_debug = value[3];
	data->time_refac = value[4];
	data->compile_required = value[5];
	data->dongle_cooldown = value[6];
	data->simulation_active = 1;
	data->start_time = get_time_ms();
	data->queue_control.first = NULL;
	data->queue_control.last = NULL;
	create_coders_and_dongle(data);
	return (0);
}

static void	create_coders_and_dongle(t_data *data)
{
	int	count;

	count = 0;
	while (data->nbr_coders != count)
	{
		data->coder[count].id = count + 1;
		data->coder[count].time_bournout = get_time_ms();
		data->coder[count].code_compiled = 0;
		data->coder[count].data = data;
		data->coder[count].left_dongle = &data->dongle[count];
		data->coder[count].right_dongle = (&data->dongle[(count + 1)
				% data->nbr_coders]);
		count++;
	}
	count = 0;
	while (data->nbr_dongle != count)
	{
		data->dongle[count].id = 'A' + count;
		data->dongle[count].cooldown = 0;
		data->dongle[count].data = data;
		count++;
	}
}
