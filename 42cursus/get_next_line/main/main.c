/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   main.c                                             :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: roandrie <roandrie@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/27 11:48:58 by roandrie          #+#    #+#             */
/*   Updated: 2025/11/04 18:05:57 by roandrie         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "get_next_line.h"
#include <fcntl.h>
#include <stdio.h>
#include <unistd.h>

int	main(int argc, char **argv)
{
	char	*next_line;
	int		count;
	int		fd;

	count = 0;
	fd = 0;
	if (argc == 1)
		fd = 0;
	else if (argc == 2)
		fd = open(argv[1], O_RDONLY);
	else
	{
		printf("Write \"./a.out\" followed by either:\n");
		printf("- A valid text file.\n");
		printf("- A string.\n");
	}
	if (fd == -1)
	{
		printf("Error opening file or incorrect file name.\n");
		return (1);
	}
	while (1)
	{
		next_line = get_next_line(fd);
		if (next_line == NULL)
		{
			printf("[NULL]\n");
			break;
		}
		count++;
		printf("[%d]: %s", count, next_line);
		free(next_line);
		next_line = NULL;
	}
	if (fd != 0)
        close(fd);
	return (0);
}

//www -D BUFFER_SIZE=3 -I . get_next_line.c get_next_line_utils.c main/main.c
