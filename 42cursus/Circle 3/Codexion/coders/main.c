/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   main.c                                             :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: roandrie <roandrie@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/02/05 17:16:12 by roandrie          #+#    #+#             */
/*   Updated: 2026/02/21 15:33:45 by roandrie         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "codexion.h"

/**
 * Program entry point.
 *
 * Initialize the 'data' structure and put memory at 0. Then, check if the
 * arguments are valid, otherwise return '1' and stop the program. If not,
 * init mutex and threads and launch the simulation. Once done, destroy all
 * created mutex, free the memory and stop the program.
 */

int	main(int argc, char **argv)
{
	t_data	data;

	memset(&data, 0, sizeof(t_data));
	if (argc != 9)
		return (print_error(print_usage(), NULL, &data));
	if (check_arg(&data, argv) == 1)
		return (1);
	init_mutex(&data);
	init_thread(&data);
	join_thread(&data);
	destroy_mutex(&data);
	free_memory(&data);
	return (0);
}
