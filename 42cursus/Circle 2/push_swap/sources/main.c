/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   main.c                                             :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: roandrie <roandrie@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/29 12:36:59 by roandrie          #+#    #+#             */
/*   Updated: 2025/11/29 14:00:33 by roandrie         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "../include/push_swap.h"

int	main(int argc, char **argv)
{
	if (argc < 1)
		return (ft_printf(2, RED"Error\nToo few arguments\n"), 1);
	convert_param(argv);
	return (0);
}
