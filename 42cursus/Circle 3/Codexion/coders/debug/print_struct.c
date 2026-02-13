/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   print_struct.c                                     :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: roandrie <roandrie@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/02/06 13:06:57 by roandrie          #+#    #+#             */
/*   Updated: 2026/02/06 15:40:59 by roandrie         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "codexion.h"

void	debug_print_struct(t_data *data)
{
	int	count;

	count = 0;
	printf("Numbers of coders: %d\n", data->nbr_coders);
	printf("Number of dongles: %d\n", data->nbr_dongle);
	printf("Time to burnout: %lldms\n", data->burnout_max);
	printf("Time to compile: %lldms\n", data->time_comp);
	printf("Time to debug: %lldms\n", data->time_debug);
	printf("Time to refactor: %lldms\n", data->time_refac);
	printf("Number of compiles required: %d\n", data->compile_required);
	printf("Dongle cooldown: %lldms\n", data->dongle_cooldown);
	printf("Scheduler: %s\n\n--Coders--\n", data->scheduler);
	while (data->nbr_coders != count)
	{
		printf("Coder: %d | %d | %lldms\n", data->coder[count].id,
			data->coder[count].code_compiled, data->coder[count].time_bournout);
		count++;
	}
	count = 0;
	while (data->nbr_dongle != count)
	{
		printf("Dongle: %c | %lldms\n", data->dongle[count].id,
			data->dongle[count].cooldown);
		count++;
	}
}
