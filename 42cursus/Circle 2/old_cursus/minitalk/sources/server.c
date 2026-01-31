/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   server.c                                           :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: roandrie <roandrie@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/01/19 11:41:23 by roandrie          #+#    #+#             */
/*   Updated: 2026/01/31 08:43:41 by roandrie         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "../include/minitalk.h"

#define SIZE_BUFFER 1024

void	print_signal(int bit)
{
	static int	i = 0;
	static int	buff_index = 0;
	static char	c = 0;
	static char	buffer[SIZE_BUFFER];

	c = c << 1 | bit;
	i++;
	if (i == 8)
	{
		buffer[buff_index++] = c;
		if (c == '\0' || c == '\n' || buff_index == SIZE_BUFFER)
		{
			if (buff_index > 0)
			{
				write(1, buffer, buff_index);
				buff_index = 0;
			}
		}
		i = 0;
		c = 0;
	}
}

void	get_signal(int signal)
{
	if (signal == SIGUSR1)
		print_signal(0);
	else
		print_signal(1);
}

int	main(void)
{
	ft_printf(1, "[Server] PID: %d\n", getpid());
	signal(SIGUSR1, get_signal);
	signal(SIGUSR2, get_signal);
	while (1)
		pause();
	return (0);
}
