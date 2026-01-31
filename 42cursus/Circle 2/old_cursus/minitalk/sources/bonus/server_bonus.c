/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   server_bonus.c                                     :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: roandrie <roandrie@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/01/30 08:23:11 by roandrie          #+#    #+#             */
/*   Updated: 2026/01/31 08:53:52 by roandrie         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "../../include/minitalk.h"

#define SIZE_BUFFER 1024

void	print_signal(int bit, int pid)
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
				kill(pid, SIGUSR1);
			}
		}
		i = 0;
		c = 0;
	}
}

void	get_signal(int signal, siginfo_t *pid, void *context)
{
	(void)context;
	if (signal == SIGUSR1)
		print_signal(0, pid->si_pid);
	else
		print_signal(1, pid->si_pid);
}

int	main(void)
{
	struct sigaction	sa;

	ft_printf(1, "[Server] PID: %d\n", getpid());
	sa.sa_sigaction = get_signal;
	sa.sa_flags = SA_SIGINFO;
	sigemptyset(&sa.sa_mask);
	sigaction(SIGUSR1, &sa, NULL);
	sigaction(SIGUSR2, &sa, NULL);
	while (1)
		pause();
	return (0);
}
