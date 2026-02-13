/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   main.c                                             :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: roandrie <roandrie@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/02/05 17:16:12 by roandrie          #+#    #+#             */
/*   Updated: 2026/02/13 11:05:28 by roandrie         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "codexion.h"

static int	init_mutex_thread(t_data *data);

int	main(int argc, char **argv)
{
	t_data	data;

	memset(&data, 0, sizeof(t_data));
	if (argc != 9)
		return (print_error(print_usage(), NULL, &data));
	if (check_arg(argv, &data) == 1)
		return (1);
	if (init_mutex_thread(&data) == 1)
		return (1);
	start_simulation(&data);
	join_thread(&data);
	free_memory(&data);
	return (0);
}

static int	init_mutex_thread(t_data *data)
{
	init_mutex_for_dongle(data);
	init_mutex_print(data);
	init_thread(data);
	return (0);
}
