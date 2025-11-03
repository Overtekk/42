/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   main.c                                             :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: roandrie <roandrie@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/27 11:48:58 by roandrie          #+#    #+#             */
/*   Updated: 2025/11/03 12:12:37 by roandrie         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "get_next_line.h"
#include <fcntl.h>
#include <stdio.h>
#include <unistd.h>

int	main()
{
	int		fd;
	char	*next_line;
	int		count;

	count = 0;
	fd = open("hello.txt", O_RDONLY);
	if (fd == -1)
	{
		printf("Error opening file");
		return (1);
	}
	while (1)
	{
		next_line = get_next_line(fd);
		if (next_line == NULL)
			break;
		count++;
		printf("[%d]: %s", count, next_line);
		free(next_line);
		next_line = NULL;
	}
	close(fd);
	return (0);
}
