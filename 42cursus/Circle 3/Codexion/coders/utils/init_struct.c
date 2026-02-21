/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   init_struct.c                                      :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: roandrie <roandrie@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/02/11 10:46:33 by roandrie          #+#    #+#             */
/*   Updated: 2026/02/21 16:34:11 by roandrie         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "codexion.h"

static void	create_coders_and_dongle(t_data *data);
static void	fill_dongle_id(char *id_str, int index);
static void	init_coders(t_data *data, t_coder *coder, int count);
static void	init_basic_data_coders(t_data *data, t_coder *coder, int count);

/**
 * Init the data structure default informations. Also create the binary tree
 * for the 'edf' scheduler.
 */

int	init_struct(t_data *data)
{
	int	i;

	data->simulation_active = 1;
	data->start_time = get_time_ms();
	data->queue_control.first = NULL;
	data->queue_control.last = NULL;
	data->heap_control.size = 0;
	i = 0;
	while (i < MAX_CODERS)
	{
		data->heap_control.tree[i] = NULL;
		i++;
	}
	create_coders_and_dongle(data);
	return (0);
}

/**
 * Give to each coders and dongles informations.
 */

static void	create_coders_and_dongle(t_data *data)
{
	int	count;

	count = 0;
	while (data->nbr_coders != count)
	{
		init_coders(data, &data->coder[count], count);
		fill_dongle_id(data->dongle[count].id, count);
		data->dongle[count].cooldown = 0;
		data->dongle[count].data = data;
		count++;
	}
}

/**
 * Create for each dongle an unique identifier started with 'A'. If there are
 * more than 26 dongles, the next one will have the identifier 'AA' and so one.
 */

static void	fill_dongle_id(char *id_str, int index)
{
	int		i;
	int		len;
	char	temp[10];

	i = 0;
	while (index >= 0)
	{
		temp[i++] = (index % 26) + 'A';
		index = (index / 26) - 1;
	}
	temp[i] = '\0';
	len = i;
	i = 0;
	while (i < len)
	{
		id_str[i] = temp[len - 1 - i];
		i++;
	}
	id_str[i] = '\0';
}

/**
 * Assign the left and right dongles to a coder. Handles deadlock prevention
 * by inverting the dongle assignment order for the last coder, and manages
 * the single coder edge case.
 */

static void	init_coders(t_data *data, t_coder *coder, int count)
{
	int	next_id;

	init_basic_data_coders(data, coder, count);
	if (data->nbr_coders > 1)
	{
		next_id = (count + 1) % data->nbr_coders;
		if (count < next_id)
		{
			coder->left_dongle = &data->dongle[count];
			coder->right_dongle = &data->dongle[next_id];
		}
		else
		{
			coder->left_dongle = &data->dongle[next_id];
			coder->right_dongle = &data->dongle[count];
		}
	}
	else
		coder->left_dongle = &data->dongle[count];
}

/**
 * Initialize the basic variables of a coder structure, such as its ID,
 * initial burnout time, and set its dongle pointers to NULL.
 */

static void	init_basic_data_coders(t_data *data, t_coder *coder, int count)
{
	coder->id = count + 1;
	coder->time_bournout = get_time_ms();
	coder->code_compiled = 0;
	coder->have_finished = 0;
	coder->data = data;
	coder->left_dongle = NULL;
	coder->right_dongle = NULL;
}
