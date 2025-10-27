/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   main.c                                             :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: roandrie <roandrie@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/27 11:48:58 by roandrie          #+#    #+#             */
/*   Updated: 2025/10/27 16:31:03 by roandrie         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "get_next_line.h"
#include <fcntl.h>
#include <stdio.h>
#include <unistd.h>

int	main()
{
	int	fd;
	char *c = malloc(6);
	int	buff;

	buff = 0;
	//int fd = open("hello.text", O_RDWR);
	fd = open("char.txt", O_RDONLY);
	buff = read(fd, c, 5);
	if (buff > 0)
		printf("Char = %s", c);
	close(fd);
	return (0);
}
