/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   main.c                                             :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: roandrie <roandrie@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/29 12:36:59 by roandrie          #+#    #+#             */
/*   Updated: 2025/12/02 19:35:10 by roandrie         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "../include/push_swap.h"

int	main(int argc, char **argv)
{
	t_data	data;

	if (argc < 2)
		return (0);
	data.stack_a = NULL;
	data.stack_b = NULL;
	if (convert_argv(argc, argv, &data) == 1)
		return (ft_error(&(data.stack_a), NULL));
	if (is_already_sort(&(data)))
		return (0);
	init_index(&(data));
	debug_print(&(data));
	ft_double_lstclear(&(data.stack_a));
	ft_double_lstclear(&(data.stack_b));
	return (0);
}
