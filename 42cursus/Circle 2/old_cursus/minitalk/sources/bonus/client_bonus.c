/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   client_bonus.c                                     :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: roandrie <roandrie@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/01/30 08:05:41 by roandrie          #+#    #+#             */
/*   Updated: 2026/01/31 08:44:12 by roandrie         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "../../include/minitalk.h"

void	send_signal(char c, int server_pid)
{
	int	i;
	int	bit;

	i = 7;
	while (i >= 0)
	{
		bit = (c >> i) & 1;
		if (bit == 0)
			kill(server_pid, SIGUSR1);
		else
			kill(server_pid, SIGUSR2);
		usleep(400);
		i--;
	}
}

void	ping(int signal)
{
	if (signal == SIGUSR1)
	{
		ft_printf(1, "Message received by the server.\n");
		exit(0);
	}
}

int	main(int argc, char **argv)
{
	int	server_pid;
	int	i;

	if (argc != 3)
		return (ft_printf(2, "ERROR (args): Use ./client <PID> <MESSAGE>."), 1);
	server_pid = ft_atoi(argv[1]);
	signal(SIGUSR1, ping);
	if (server_pid <= 0 || kill(server_pid, 0) == -1)
		return (ft_printf(2, "ERROR: Incorrect PID"), 1);
	i = 0;
	while (argv[2][i] != '\0')
	{
		send_signal(argv[2][i], server_pid);
		i++;
	}
	send_signal('\n', server_pid);
	send_signal('\0', server_pid);
	while (1)
		pause();
	return (0);
}
