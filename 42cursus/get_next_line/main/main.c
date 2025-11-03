/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   main.c                                             :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: roandrie <roandrie@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/27 11:48:58 by roandrie          #+#    #+#             */
/*   Updated: 2025/10/28 14:14:54 by roandrie         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "get_next_line.h"
#include <fcntl.h>
#include <stdio.h>
#include <unistd.h>

int	main()
{
	int	fd;
	char *result;

	fd = open("hello.txt", O_RDONLY);
	if (fd == -1)
		return (2);
	result = get_next_line(fd);
	printf("%s", result);
	//free (result);
	close(fd);
	return (0);
}
